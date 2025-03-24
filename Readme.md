## FunctionVisualizer 사용법

### 목적
재귀함수들이 반복해서 호출되는 과정을 시각적으로 보여줘서 재귀함수를 좀 더 쉽게 이해할 수 있도록 하는 것입니다.

### 설치방법
1. graphviz 설치
https://graphviz.org/에 방문해서 다운로드 방법에 따라서 설치

2. Python용 graphviz 라이브러리를 설치
* virtualenv나 conda를 사용하여 개발중일 경우 그 가상 환경을 활성화 시킵니다. 
* 아래 명령어를 이용해서 graphviz 라이브러리를 설치합니다.
    ```
    pip install graphviz
    ```

3. functionVisualizer 프로그램을 다운로드 합니다. 
    ```
    git clone https://github.com/krafton-jungle/functionVisualizer
    ```

4. 시각화하려는 프로그램 코드가 있는 폴더에 functionVisualizer프로그램의 function_visualizer.py 파일을 복사합니다.

5. 만약 fib 함수를 시각화 하려면 아래와 같이 작성합니다. 
    ```
    from function_visualizer import FunctionVisualizer    
    visualizer = FunctionVisualizer()

    @visualizer.visualize(param_names=["n"])
    def fib(n):
        if n <= 1:
            return n
        else:
            return fib(n-1) + fib(n-2)
    
    result = fib(10)

    visualizer.render("fib")
    ```
    * FunctionVisualizer를 임포트합니다.
    ```
    from function_visualizer import FunctionVisualizer 
    ```
    * FunctionVisualizer객체를 만듭니다. 재귀함수가 정의된 파일에 한번만 하면 됩니다.  
    ```
    visualizer = FunctionVisualizer()
    ```
    * 시각화하려는 재귀함수마다 @visualize.visualize를 추가합니다. 
    ```
    @visualizer.visualize(param_names=["n"])
    ```
    여기서 param_names에는 시각화할 재귀함수의 패러미터를 정의합니다. 재귀함수가 호출될때 변화되는 값만 알고 싶으면 그 패러미터 이름만 추가하면 됩니다. 만약 모든 패러미터를 시각화하고 싶으면 param_names 없이 아래와 같이 정의하면 됩니다.
    ```
    @visualizer.visualize()
    ```
6. 이제 재귀함수를 호출하고 그 결과를 시각화하기 위해서 아래와 같이 파일에 저장하면 됩니다.
    ```
    visualizer.render("explusive_string")
    ```

### 전체 소스코드 예제
```
# FunctionVisualizer 클래스 임포트
from function_visualizer import FunctionVi성ualizer

# 시각화 객체 생트
visualizer = FunctionVisualizer()

# 피보나치 수열 함수에 visualizer 정의
@visualizer.visualize(param_names=["n"])
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# 피보나치 함수 실행
result = fibonacci(5)
print(f"결과: {result}")

# 그래프 저장
visualizer.render("fibonacci_calls")
```