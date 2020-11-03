
def env(CurrentEnvironment):
    if CurrentEnvironment == 'test':
        CurrentHost = "http://xcds.test.17zuoye.net/"
    elif CurrentEnvironment == 'staging':
        CurrentHost = "https://xcds.staging.17zuoye.net/"
    elif CurrentEnvironment == 'pro':
        CurrentHost = "https://xcds.17zuoye.com/"
    else:
        print("地址不存在！请核实：%s" %(CurrentEnvironment))

    return CurrentHost