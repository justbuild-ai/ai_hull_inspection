def main():
    parser = argparse.ArgumentParser(description="AI Hull Inspection CLI")
    parser.add_argument(
        "--domain",
        required=True,
        choices=DOMAIN_HANDLERS.keys(),
        help="Target system: lv, sv, or pl",
    )
    parser.add_argument("--image", help="Path to input image")
    parser.add_argument("--model", default=MODEL_PATH, help="Path to .hef model")
    parser.add_argument("--live", action="store_true", help="Capture image from camera")

    args = parser.parse_args()

    handler = DOMAIN_HANDLERS.get(args.domain)
    if handler:
        handler(image_path=args.image, model_path=args.model, live=args.live)
    else:
        print(f"Unknown domain: {args.domain}")
