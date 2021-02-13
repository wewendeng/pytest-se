import os
import pytest

if __name__ == '__main__':
    # 获取测试用例目录
    path = os.path.dirname(__file__) + '/testcases'
    pytest.main(['-v', path])
