m0 = "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다."
m1 = "\"재귀함수가 뭔가요?\""
m2 = "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어."
m3 = "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지."
m4 = "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\""
m5 = "라고 답변하였지."
m6 = "\"재귀함수는 자기 자신을 호출하는 함수라네\""

def fun(this):
    if(this == 1 + n):
        return
    
    if(this == n):
        print(f"{'_' * 4 * this}{m1}")
        print(f"{'_' * 4 * this}{m6}")
    else:
    
        print(f"{'_' * 4 * this}{m1}")
        print(f"{'_' * 4 * this}{m2}")
        print(f"{'_' * 4 * this}{m3}")
        print(f"{'_' * 4 * this}{m4}")
        
        fun(this + 1)
    
    print(f"{'_' * 4 * this}{m5}")


n = int(input())

print(m0)

fun(0)
