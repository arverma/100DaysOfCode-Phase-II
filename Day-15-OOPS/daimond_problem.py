class A:
    def run(self):
        print("class A")

class B:
    def run(self):
        print("class B")

class C(A, B):
    pass

obj = C()
obj.run()
# class A
