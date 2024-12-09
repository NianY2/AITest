import utils.glo as glo
import glo2
glo._init()

test = glo2.Test(1)
print('is_login：',glo.get_value('is_login'))
print(glo.get_value('is_login')())