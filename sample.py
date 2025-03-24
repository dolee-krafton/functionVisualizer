# FunctionVisualizer 클래스 임포트
from function_visualizer import FunctionVisualizer

# 시각화 객체 생트
visualizer = FunctionVisualizer()


# 피보나치 수열 함수에 visualizer 정의
@visualizer.visualize(param_names=["n"])
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    # 피보나치 함수 실행
    result = fibonacci(5)
    print(f"결과: {result}")

    # 그래프 저장
    visualizer.render("fibonacci_calls")
