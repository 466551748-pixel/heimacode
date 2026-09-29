a = float(input("请输入您的体温:\n"))
def auto(data):
    print("欢迎来到深圳！请出示您的健康码以及72小时核酸证明，并配合测量体温！")
    if data <= 37.3:
        print(f"体温测量中，您的体温是；{data}，体温正常，请进")
    else:
        print(f"体温测量中，您的体温是：{data}，需要隔离")
auto(a)