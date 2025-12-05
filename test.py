def first():
    def second():
        a= "second"
        print("when it is working")
        return a
    return second


first()
        