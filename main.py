import os
import cv2
import torch
import argparse
import torch.backends.cudnn as cudnn

from hrnet.default import _C as cfg, update_config
from hrnet.pose_hrnet import get_pose_net
from hrnet.util import get_max_preds


def get_args_parser():
    parser = argparse.ArgumentParser('Set Params', add_help=False)

    parser.add_argument('--model_path', default='./weights/fhrnet.pt', type=str)
    parser.add_argument('--data_dir', default='./source', type=str)
    parser.add_argument('--output_dir', default='./outputs', type=str)

    return parser


def setup_model(args):
    update_config(cfg, args)
    cudnn.benchmark = cfg.CUDNN.BENCHMARK
    torch.backends.cudnn.deterministic = cfg.CUDNN.DETERMINISTIC
    torch.backends.cudnn.enabled = cfg.CUDNN.ENABLED
    cfg['FULL'] = True

    model = get_pose_net(cfg, is_train=False)
    return model


def inference_image(img, model, device):
    IMG_WIDTH, IMG_HEIGHT = 448, 448
    img = cv2.resize(img, (IMG_WIDTH, IMG_HEIGHT))
    img = torch.from_numpy(img.transpose((2, 0, 1))).float()
    img = img.unsqueeze(0)

    img = img.to(device)

    outputs = model.forward(img)
    outputs = outputs
    outputs = outputs.detach().cpu().numpy()

    predictions, _ = get_max_preds(outputs)

    predictions = predictions[0]

    predictions[:, 0] = predictions[:, 0] / IMG_WIDTH
    predictions[:, 1] = predictions[:, 1] / IMG_HEIGHT

    return predictions


def draw_prediction(img, predictions):
    for pred in predictions:
        img = cv2.circle(img, (int(pred[0] * img.shape[1]), int(pred[1] * img.shape[0])),
                         radius=3, color=(0, 0, 255), thickness=-1)
    return img


def main(args):
    os.makedirs(args.output_dir, exist_ok=True)

    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    model = setup_model(args)
    model.to(device)
    model.load_state_dict(torch.load(args.model_path, map_location=device))
    model.eval()

    with torch.set_grad_enabled(False):
        for img_path in os.listdir(args.data_dir):
            if img_path.endswith('.jpg') or img_path.endswith('.png') or img_path.endswith('.jpeg'):
                img = cv2.imread(f'{args.data_dir}/{img_path}')
                predictions = inference_image(img, model, device)

                img = draw_prediction(img, predictions)

                cv2.imwrite(f'{args.output_dir}/{img_path}', img)


if __name__ == '__main__':
    main(get_args_parser().parse_args())
