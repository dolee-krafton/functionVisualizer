import functools
import inspect

import graphviz


class FunctionVisualizer:
    def __init__(self):
        self.dot = graphviz.Digraph()
        self.call_stack = []
        self.call_count = 0

    def visualize(self, func=None, *, param_names=None):
        """
        함수 호출 과정을 시각화하는 데코레이터

        Args:
            func: 데코레이트할 함수
            param_names: 시각화할 매개변수 이름 리스트. None일 경우 모든 매개변수 표시
        """

        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                # 현재 노드 이름과 라벨 생성
                self.call_count += 1
                current_id = f"call_{self.call_count}"

                # 함수 이름과 인자들을 문자열로 변환
                func_name = func.__name__

                # 매개변수 필터링
                if param_names is not None:
                    # 매개변수 이름과 값을 매핑
                    arg_names = inspect.getfullargspec(func).args
                    arg_dict = dict(zip(arg_names, args))
                    arg_dict.update(kwargs)

                    # 지정된 매개변수만 포함
                    filtered_args = {
                        k: arg_dict[k] for k in param_names if k in arg_dict
                    }
                    args_str = ", ".join(f"{k}={v!r}" for k, v in filtered_args.items())
                else:
                    # 기존 방식대로 모든 매개변수 표시
                    args_str = ", ".join(repr(arg) for arg in args)
                    kwargs_str = ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
                    args_str = (
                        args_str
                        + (", " if args_str and kwargs_str else "")
                        + kwargs_str
                    )

                # 노드 라벨 생성
                label = f"{func_name}({args_str})"

                # 노드 추가
                self.dot.node(current_id, label=label)

                # 부모 노드가 있으면 엣지 추가
                if self.call_stack:
                    self.dot.edge(self.call_stack[-1], current_id)

                # 현재 노드를 콜 스택에 추가
                self.call_stack.append(current_id)

                # 함수 실행
                result = func(*args, **kwargs)

                # 콜 스택에서 현재 노드 제거
                self.call_stack.pop()

                return result

            return wrapper

        # 직접 함수가 전달된 경우(@visualize)
        if func is not None:
            return decorator(func)
        # 인자가 있는 데코레이터로 사용된 경우(@visualize(param_names=["n"]))
        return decorator

    def render(self, filename="function_calls", format="png"):
        """
        생성된 그래프를 파일로 저장
        """
        self.dot.render(filename, format=format, cleanup=True)
        return filename + "." + format


# 사용 예시
def example():
    # 시각화 객체 생성
    visualizer = FunctionVisualizer()

    # 피보나치 함수 정의 및 데코레이팅 - 특정 매개변수만 표시
    @visualizer.visualize(param_names=["n"])
    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    # 함수 실행
    result = fibonacci(5)
    print(f"결과: {result}")

    # 그래프 저장
    visualizer.render("fibonacci_calls")


if __name__ == "__main__":
    example()
