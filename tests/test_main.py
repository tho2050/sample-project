from sample import main


def test_main_prints_message(capsys):
    main()
    captured = capsys.readouterr()
    assert "Call your main application code here" in captured.out