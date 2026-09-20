from docs.knowledge_cli import build_parser

def test_cli_parser_accepts_export_options():
    args=build_parser().parse_args(["docs","out.jsonl","--max-chars","900"])
    assert str(args.root)=="docs"
    assert str(args.destination)=="out.jsonl"
    assert args.max_chars==900

def test_cli_parser_has_reproducible_default_limit():
    args=build_parser().parse_args(["docs","out.jsonl"])
    assert args.max_chars==1200
