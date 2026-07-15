from src.main import main, parse_args


def test_parse_args_reads_count():
    args = parse_args(["--count", "10"])
    assert args.count == 10


def test_main_with_negative_count_prints_error_without_crashing(capsys):
    main(["--count", "-1"])
    captured = capsys.readouterr()
    assert "오류" in captured.out
