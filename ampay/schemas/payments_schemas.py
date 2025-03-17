from enum import Enum
from uuid import UUID
from datetime import datetime

from pydantic import BaseModel


class Type(str, Enum):
    DEPOSIT = "DEPOSIT"
    WITHDRAWAL = "WITHDRAWAL"
    REFUND = "REFUND"
    CARDVERIFY = "CARDVERIFY"


class Method(str, Enum):
    ADVCASH = "ADVCASH"
    ALIPAY = "ALIPAY"
    ALYCEPAY = "ALYCEPAY"
    APPLEPAY = "APPLEPAY"
    ASTROPAY = "ASTROPAY"
    ASUPAY = "ASUPAY"
    B2BINPAY = "B2BINPAY"
    BANKTRANSFER = "BANKTRANSFER"
    BASIC_CARD = "BASIC_CARD"
    BEELINE = "BEELINE"
    BILLLINE = "BILLLINE"
    BITEXPRO_GOOGLEPAY = "BITEXPRO_GOOGLEPAY"
    BITEXPRO_CASH = "BITEXPRO_CASH"
    BITEXPRO_EWALLET = "BITEXPRO_EWALLET"
    BITEXPRO_PAYSAFECARD = "BITEXPRO_PAYSAFECARD"
    BITEXPRO_PAYSAFECASH = "BITEXPRO_PAYSAFECASH"
    BITEXPRO_RAPID = "BITEXPRO_RAPID"
    BITEXPRO_BLIK = "BITEXPRO_BLIK"
    BITEXPRO_PAPARA = "BITEXPRO_PAPARA"
    BITEXPRO = "BITEXPRO"
    BITEXPRO_ADVCARD = "BITEXPRO_ADVCARD"
    BITEXPRO_ADVWALLET = "BITEXPRO_ADVWALLET"
    BITEXPRO_APPLEPAY = "BITEXPRO_APPLEPAY"
    BITEXPRO_BPWALLET = "BITEXPRO_BPWALLET"
    BITEXPRO_CRYPTO = "BITEXPRO_CRYPTO"
    BITEXPRO_EXPAY = "BITEXPRO_EXPAY"
    BITEXPRO_GIROPAY = "BITEXPRO_GIROPAY"
    BITEXPRO_HSP = "BITEXPRO_HSP"
    BITEXPRO_NETELLER = "BITEXPRO_NETELLER"
    BITEXPRO_OPENBANK = "BITEXPRO_OPENBANK"
    BITEXPRO_PAYEER = "BITEXPRO_PAYEER"
    BITEXPRO_P2P = "BITEXPRO_P2P"
    BITEXPRO_PAYCO = "BITEXPRO_PAYCO"
    BITEXPRO_PAYFIX = "BITEXPRO_PAYFIX"
    BITEXPRO_SKRILL = "BITEXPRO_SKRILL"
    BITEXPRO_SOFORT = "BITEXPRO_SOFORT"
    BITEXPRO_STICPAY = "BITEXPRO_STICPAY"
    BITEXPRO_OPENBANKING = "BITEXPRO_OPENBANKING"
    BLIK = "BLIK"
    BOLETO = "BOLETO"
    CARDSHPP = "CARDSHPP"
    CASH = "CASH"
    CHEK = "CHEK"
    CLICK = "CLICK"
    COMMUNITYBANKING = "COMMUNITYBANKING"
    CRYPTO = "CRYPTO"
    DANA = "DANA"
    DEBITWAY = "DEBITWAY"
    EFECTY = "EFECTY"
    EFT = "EFT"
    EMPAYRE = "EMPAYRE"
    EPAY = "EPAY"
    EWALLET = "EWALLET"
    EZPAY = "EZPAY"
    FLEXEPIN = "FLEXEPIN"
    FPS = "FPS"
    GATESTRANSACT = "GATESTRANSACT"
    GATEEXPRESS = "GATEEXPRESS"
    GCASH = "GCASH"
    GIROPAY = "GIROPAY"
    GOOGLEPAY = "GOOGLEPAY"
    HAVALE = "HAVALE"
    HAYHAY = "HAYHAY"
    HITES = "HITES"
    IBAN = "IBAN"
    IDEAL = "IDEAL"
    INSTANTQR = "INSTANTQR"
    INTERAC = "INTERAC"
    KAKAOPAY = "KAKAOPAY"
    KCELL = "KCELL"
    KESSPAY = "KESSPAY"
    KHIPU = "KHIPU"
    KHIPUBANKTRANSFER = "KHIPUBANKTRANSFER"
    LATAM_CASH = "LATAM_CASH"
    LINK_AJA = "LINK_AJA"
    LOCALP2P = "LOCALP2P"
    LOCALPAYMENT = "LOCALPAYMENT"
    LOTERICA = "LOTÉRICA"
    MACH = "MACH"
    MACROPAY = "MACROPAY"
    MB = "MB"
    MBWAY = "MBWAY"
    MISTERCASH = "MISTERCASH"
    MOBILE = "MOBILE"
    MOBILEMONEY = "MOBILEMONEY"
    MOBILEMONEY_AIRTEL = "MOBILEMONEY_AIRTEL"
    MOBILEMONEY_BANKTRANSFER = "MOBILEMONEY_BANKTRANSFER"
    MOBILEMONEY_MPESA = "MOBILEMONEY_MPESA"
    MOBILEMONEY_MTN = "MOBILEMONEY_MTN"
    MOBILEMONEY_ORANGE = "MOBILEMONEY_ORANGE"
    MOBILEMONEY_OZOW = "MOBILEMONEY_OZOW"
    MOBILEMONEY_SNAPSCAN = "MOBILEMONEY_SNAPSCAN"
    MOBILEMONEY_VODAFONE = "MOBILEMONEY_VODAFONE"
    MOBILEMONEY_WAVE = "MOBILEMONEY_WAVE"
    MOBILEMONEY_ZAMTEL = "MOBILEMONEY_ZAMTEL"
    MONETIX = "MONETIX"
    MONNET = "MONNET"
    MULTIBANCO = "MULTIBANCO"
    NETBANKING = "NETBANKING"
    NETELLER = "NETELLER"
    NGENIUS = "NGENIUS"
    ONLINEBANKING = "ONLINEBANKING"
    ONLINEBANKINGBTV = "ONLINEBANKINGBTV"
    OPENBANKING = "OPENBANKING"
    OVO = "OVO"
    OXXO = "OXXO"
    P24 = "P24"
    P2C = "P2C"
    PAGO_EFECTIVO = "PAGO_EFECTIVO"
    PAGOFFECTIVOCASH = "PAGOFFECTIVOCASH"
    PAGOFFECTIVOONLINE = "PAGOFFECTIVOONLINE"
    PAPARA = "PAPARA"
    PAPARAPOOL = "PAPARAPOOL"
    PAYBOL = "PAYBOL"
    PAYCELL = "PAYCELL"
    PAYCO = "PAYCO"
    PAYCOS = "PAYCOS"
    PAYFIX = "PAYFIX"
    PAYID = "PAYID"
    PAYMAXIS = "PAYMAXIS"
    PAYMAYA = "PAYMAYA"
    PAYPAL = "PAYPAL"
    PAYRETAILERS = "PAYRETAILERS"
    PAYRIVER = "PAYRIVER"
    PAYSAFECARD = "PAYSAFECARD"
    PAYSAFECASH = "PAYSAFECASH"
    PAYTM = "PAYTM"
    PEP = "PEP"
    PERFECTMONEY = "PERFECTMONEY"
    PICPAY = "PICPAY"
    PIX = "PIX"
    POLI = "POLI"
    PRZELEWY24 = "PRZELEWY24"
    PSEBANKTRANSFER = "PSEBANKTRANSFER"
    QRCODE = "QRCODE"
    RAPID_TRANSFER = "RAPID_TRANSFER"
    RAPIDTRANSFER = "RAPIDTRANSFER"
    RAPYD = "RAPYD"
    RETAILCARD = "RETAILCARD"
    SAFETYPAY = "SAFETYPAY"
    SAMSUNGPAY = "SAMSUNGPAY"
    SEPA = "SEPA"
    SKRILL = "SKRILL"
    SLYSE = "SLYSE"
    SOFORT = "SOFORT"
    SPEI = "SPEI"
    SPELL = "SPELL"
    STRIPE = "STRIPE"
    SWIFT = "SWIFT"
    TINK = "TINK"
    TODITO = "TODITO"
    TPAGA = "TPAGA"
    TRUEMONEY = "TRUEMONEY"
    TRUSTLY = "TRUSTLY"
    TRUSTPAYMENTS = "TRUSTPAYMENTS"
    UNIONPAYCARDS = "UNIONPAYCARDS"
    UPI = "UPI"
    VIETQR = "VIETQR"
    VIETTELPAY = "VIETTELPAY"
    VIRTUALACCOUNT = "VIRTUALACCOUNT"
    VOLT = "VOLT"
    VOUCHERS = "VOUCHERS"
    VOUCHSTAR = "VOUCHSTAR"
    WEBPAY = "WEBPAY"


class State(str, Enum):
    COMPLETED = "COMPLETED"
    PENDING = "PENDING"
    CANCELLED = "CANCELLED"
    DECLINED = "DECLINED"
    CHECKOUT = "CHECKOUT"
    ERROR = "ERROR"
    RECONCILIATION = "RECONCILIATION"
    AWAITING_WEBHOOK = "AWAITING_WEBHOOK"
    AWAITING_REDIRECT = "AWAITING_REDIRECT"
    AWAITING_APPROVAL = "AWAITING_APPROVAL"
    AWAITING_RETURN = "AWAITING_RETURN"
    CASCADING_CONFIRMATION = "CASCADING_CONFIRMATION"


class Currency(str, Enum):
    USD = "USD"  # Доллар США
    EUR = "EUR"  # Евро
    GBP = "GBP"  # Фунт стерлингов
    JPY = "JPY"  # Японская йена
    CNY = "CNY"  # Китайский юань
    INR = "INR"  # Индийская рупия
    AUD = "AUD"  # Австралийский доллар
    CAD = "CAD"  # Канадский доллар
    CHF = "CHF"  # Швейцарский франк
    RUB = "RUB"  # Российский рубль
    BRL = "BRL"  # Бразильский реал
    KRW = "KRW"  # Южнокорейская вона
    MXN = "MXN"  # Мексиканский песо
    SGD = "SGD"  # Сингапурский доллар
    HKD = "HKD"  # Гонконгский доллар
    NZD = "NZD"  # Новозеландский доллар
    SEK = "SEK"  # Шведская крона
    NOK = "NOK"  # Норвежская крона
    DKK = "DKK"  # Датская крона
    ZAR = "ZAR"  # Южноафриканский рэнд
    TRY = "TRY"  # Турецкая лира
    AED = "AED"  # Дирхам ОАЭ
    SAR = "SAR"  # Саудовский риял
    THB = "THB"  # Тайский бат
    MYR = "MYR"  # Малайзийский ринггит
    IDR = "IDR"  # Индонезийская рупия
    PHP = "PHP"  # Филиппинское песо
    PLN = "PLN"  # Польский злотый
    CZK = "CZK"  # Чешская крона
    HUF = "HUF"  # Венгерский форинт
    ILS = "ILS"  # Израильский шекель
    ARS = "ARS"  # Аргентинское песо
    CLP = "CLP"  # Чилийское песо
    COP = "COP"  # Колумбийское песо
    PEN = "PEN"  # Перуанский соль
    VND = "VND"  # Вьетнамский донг
    PKR = "PKR"  # Пакистанская рупия
    BDT = "BDT"  # Бангладешская така
    KZT = "KZT"  # Казахстанский тенге
    UAH = "UAH"  # Украинская гривна
    QAR = "QAR"  # Катарский риал
    KWD = "KWD"  # Кувейтский динар
    BHD = "BHD"  # Бахрейнский динар
    OMR = "OMR"  # Оманский риал
    LKR = "LKR"  # Шри-Ланкийская рупия
    NPR = "NPR"  # Непальская рупия
    EGP = "EGP"  # Египетский фунт
    MAD = "MAD"  # Марокканский дирхам
    TWD = "TWD"  # Тайваньский доллар
    CRC = "CRC"  # Коста-риканский колон
    DOP = "DOP"  # Доминиканское песо
    UYU = "UYU"  # Уругвайское песо
    PYG = "PYG"  # Парагвайский гуарани
    BOB = "BOB"  # Боливийский боливиано
    GTQ = "GTQ"  # Гватемальский кетсаль
    HNL = "HNL"  # Гондурасская лемпира
    NIO = "NIO"  # Никарагуанская кордоба
    SVC = "SVC"  # Сальвадорский колон
    JMD = "JMD"  # Ямайский доллар
    TTD = "TTD"  # Доллар Тринидада и Тобаго
    BBD = "BBD"  # Барбадосский доллар
    AWG = "AWG"  # Арубанский флорин
    BSD = "BSD"  # Багамский доллар
    BZD = "BZD"  # Белизский доллар
    KYD = "KYD"  # Доллар Каймановых островов
    XCD = "XCD"  # Восточно-карибский доллар
    ANG = "ANG"  # Нидерландский антильский гульден
    FJD = "FJD"  # Фиджийский доллар
    WST = "WST"  # Самоанская тала
    TOP = "TOP"  # Тонганская паанга
    VUV = "VUV"  # Вануатский вату
    PGK = "PGK"  # Папуа-новогвинейская кина
    SBD = "SBD"  # Доллар Соломоновых островов
    ZMW = "ZMW"  # Замбийская квача
    MWK = "MWK"  # Малавийская квача
    GHS = "GHS"  # Ганский седи
    XOF = "XOF"  # Франк КФА BCEAO
    XAF = "XAF"  # Франк КФА BEAC
    KMF = "KMF"  # Коморский франк
    DJF = "DJF"  # Джибутийский франк
    GNF = "GNF"  # Гвинейский франк
    MGA = "MGA"  # Малагасийский ариари
    MUR = "MUR"  # Маврикийская рупия
    SCR = "SCR"  # Сейшельская рупия
    CDF = "CDF"  # Конголезский франк
    RWF = "RWF"  # Руандийский франк
    UGX = "UGX"  # Угандийский шиллинг
    TZS = "TZS"  # Танзанийский шиллинг
    ETB = "ETB"  # Эфиопский быр
    SOS = "SOS"  # Сомалийский шиллинг
    BIF = "BIF"  # Бурундийский франк
    GMD = "GMD"  # Гамбийский даласи
    MRO = "MRO"  # Мавританская угия
    STD = "STD"  # Сан-Томейская добра
    AOA = "AOA"  # Ангольская кванза
    NAD = "NAD"  # Намибийский доллар
    SZL = "SZL"  # Свазилендский лилангени
    LSL = "LSL"  # Лесотский лоти
    ERN = "ERN"  # Эритрейская накфа
    SSP = "SSP"  # Южносуданский фунт
    TND = "TND"  # Тунисский динар
    LYD = "LYD"  # Ливийский динар
    DZD = "DZD"  # Алжирский динар
    SDG = "SDG"  # Суданский фунт
    KES = "KES"  # Кенийский шиллинг
    BWP = "BWP"  # Ботсванская пула
    ZWL = "ZWL"  # Зимбабвийский доллар
    MZN = "MZN"  # Мозамбикский метикал
    AMD = "AMD"  # Армянский драм
    AZN = "AZN"  # Азербайджанский манат
    BYN = "BYN"  # Белорусский рубль
    GEL = "GEL"  # Грузинский лари
    MDL = "MDL"  # Молдавский лей
    TJS = "TJS"  # Таджикский сомони
    TMT = "TMT"  # Туркменский манат
    UZS = "UZS"  # Узбекский сум
    KGS = "KGS"  # Киргизский сом
    AFN = "AFN"  # Афганский афгани
    IRR = "IRR"  # Иранский риал
    IQD = "IQD"  # Иракский динар
    SYP = "SYP"  # Сирийский фунт
    YER = "YER"  # Йеменский риал
    LBP = "LBP"  # Ливанский фунт
    JOD = "JOD"  # Иорданский динар
    BND = "BND"  # Брунейский доллар
    FKP = "FKP"  # Фунт Фолклендских островов
    GIP = "GIP"  # Гибралтарский фунт
    SHP = "SHP"  # Фунт Святой Елены
    IMP = "IMP"  # Мэнский фунт


class SPaymentCreate(BaseModel):
    referenceId: str
    type: Type = Type.DEPOSIT
    method: Method = Method.BASIC_CARD
    amount: float
    currency: Currency
    description: str


class SPaymentDisplay(BaseModel):
    id: UUID
    referenceId: str
    type: Type
    method: Method
    amount: float
    currency: Currency
    description: str
    createdAt: datetime
    state: State


class SPaginationPayments(BaseModel):
    payments: list[SPaymentDisplay]
    totalCount: int
    currentCount: int
