from time import sleep
import emoji

for i in range(10 , -1, -1):
    print(i)
    sleep(1)
print(emoji.emojize(':sparkler::fireworks: HAPPY NEW YEAR :fireworks::sparkler:', language='alias'))