COMMAND PATTERN
===============


* 커맨드 패턴은 Command와 Receiver, Invoker, Client 클래스로 구성된다.
    * Command 객체는 Receiver 객체에 대해 알고 있으며 Receiver 객체의 함수를 호출한다.
    * Receiver 함수의 인자는 Command 객체에 저장돼 있다.
    * Invoker는 명령을 수행한다.
    * Client는 Command 객체를 생성하고 Receiver를 정한다.


* 커맨드 패턴의 목적은 다음과 같다.
    * 요청을 객체 속에 캡슐화한다.
    * 클라이언트의 다양한 요청을 매개변수화한다.
    * 요청을 큐에 저장한다.
    * 객체지향 콜백을 지원한다.

* 커맨드 패턴은 다음과 같은 상황에 적합하다.
    * 수행할 명령에 따라 객체를 변수화할 때
    * 요청을 큐에 저장하고 각기 다른 시점에 수행해야 하는 경우
    * 작은 단위의 연산을 기반으로 하는 상위 연산을 만들 때


----

세부적인 객체 정의
    1. Command: 연산을 수행할 인터페이스를 정의한다.
    2. ConcreteCommand: Receiver 객체와 연산 간 바인딩을 정의한다.
    3. Client: ConcreteCommand 객체를 생성하고 Receiver를 설정한다.
    4. Invoker: ConcreteCommand에 수행을 요청한다.
    5. Receiver: 요청에 관련된 연산을 관리한다.

.. Important:: 전체적인 흐름은 단순하다. 클라이언트는 특정 연산을 요청하고 Invoker는 요청을 받아 캡슐화해 큐에 넣는다.
    ConcreteCommand 클래스는 이 요청을 책임지고 Receiver에 수행을 맡긴다.