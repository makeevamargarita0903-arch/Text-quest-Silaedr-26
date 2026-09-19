import time

def final_scene(tests, inventory):
    time.sleep(2)
    print('\n=== ФИНАЛ ===')
    time.sleep(1.5)
    if tests == 0:
        print('Ты справился со всеми долгами по заданиям!')
    elif tests <= 5:
        print('Ты почти справился, осталось совсем немного заданий…')
    else:
        print('Заданий ещё много, но ты точно не сдался!')
    time.sleep(2)
    print('История подошла к концу.')
    time.sleep(2)
    if inventory:
        print('Твой финальный инвентарь:', ', '.join(inventory.keys()))
    else:
        print('Твой инвентарь пуст.')
    time.sleep(1.5)
    print('Спасибо, что прошёл этот квест!')
