import pickle
import random
with open('data', 'rb') as f:
    f = pickle.load(f)
quotes = ['The true sign of intelligence is not knowledge but imagination.', 'I have no special talent. I am only passionately curious.', 'If you got language, You got key to the world.', 'To live is to risk it all.', 'Nobody exists on purpose.', 'If you spend all day shuffling words around, you can make anything sound bad.', 'But what people calls “love” is just a chemical reaction that compels animals to breed. It hits hard, Morty, then it slowly fades, leaving you stranded in a failing marriage.', 'Love your Enemies, for they tell you your Faults.', "Look before, or you'll find yourself behind.", 'Better slip with foot than tongue.', 'Time is money.', 'Stay hungry. Stay Foolish', 'Have the courage to follow your heart and intuition.', 'Nothing matters.', 'Keep your face to the sun and you will never see the shadows.', 'Question everything.', "Everybody's gonna die.", "Pain doesn't tell you when you ought to stop.", 'Have you seen Los Angeles at 4am?', 'Imagine you can understand most people in the world.', 'Make everyday you live the last day of your life.', "Don't care what others said.They are just others.", 'The way I see it, if you want the rainbow, you gotta put up with the rain.', 'The day goes on.', "Everybody is alone.But it doesn't means you can't be happy.", 'How could this happen?I made my mistakes, got nowhere to run, the night goes on.', "As I'm fading away.....", 'I just wanna scream']
for i, content in f.items():
    with open("../Lessons/Lesson-%d.md"%i, 'w') as m:
        m.write('## Lesson %d\n'%i)
        m.write('> %s\n\n'%quotes.pop(0))
        m.write('| Word | Meaning |\n')
        m.write('| ---- | ---- |\n')
        for w, c in content:
            m.write('| %s | %s |\n'%(w, c))
