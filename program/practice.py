import pickle, os, datetime
def get_index():
    try:
        x = input("Enter index: ").split(',')
        x = [int(i) for i in x]
    except:
        x = get_index()
    return x

class Lesson:
    def __init__(self, data):
        self.data = data
        self.learned = False
    def practice(self):
        if self.learned:
            for i, m in self.new:
                print(i, m)
                input()
                os.system('clear')
                mainloop()

        else:
            for i in range(0, 100, 10):
                index = 0
                d = self.data[i:i+10]
                for b, x in d:
                    print('{:3}   {:20}{}'.format(index, b, x)); index+=1
                self.new = [d[i] for i in get_index()]
                os.system('clear')
            with open('lessons', 'wb') as f:
                    pickle.dump(lessons, f)
            self.learned = True
            mainloop()

if os.path.exists('lessons'):
    with open('lessons', 'rb') as _:
        lessons = _
else:
    with open('data', 'rb') as f:
        f = pickle.load(f)
    lessons = {i:Lesson(m) for i, m in f.items()}

def mainloop():
    for i in range(1, 29):
        print("Lesson %d  "%i, end='')
        print("√"if lessons[i].learned else "X")
    lessons[int(input("Pick one: "))].practice()

mainloop()