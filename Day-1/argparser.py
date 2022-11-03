import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--a",
        help="specify full path of config file",
        action="store",
        required=True,
    )
    parser.add_argument("--b", type=int, help="Yearmo", required=False)
    print(parser.parse_known_args())
    return parser.parse_known_args()[0]


def parse_args_org():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--a",
        help="specify full path of config file",
        action="store",
        required=True,
    )
    parser.add_argument("--b", type=int, help="Yearmo", required=False)
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    print(args.a)
    print(args.b)
    # args_org = parse_args_org()
    # print(args_org, args_org.a)
