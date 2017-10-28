from slippery import decorators


def test_execution_time(capsys):
    @decorators.execution_time
    def test():
        return True
    test()
    out, err = capsys.readouterr()
    assert 'Total execution time' in out


def test_disassemble(capsys):
    @decorators.disassemble
    def test():
        return True
    test()
    out, err = capsys.readouterr()
    assert 'LOAD_CONST' in out
    assert 'RETURN_VALUE' in out


def test_efficiency(capsys):
    @decorators.efficiency
    def test():
        return True
    test()
    out, err = capsys.readouterr()
    assert 'function calls' in out
    assert 'ncalls' in out
