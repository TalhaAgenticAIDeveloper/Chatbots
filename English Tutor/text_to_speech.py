
import asyncio
import edge_tts
import pygame

VOICES = [
    "af-ZA-AdriNeural", "af-ZA-WillemNeural","am-ET-MekdesNeural", "am-ET-AmehaNeural",
    "ar-AE-FatimaNeural", "ar-AE-HamdanNeural","ar-BH-AliNeural", "ar-BH-LailaNeural",
    "ar-DZ-AminaNeural", "ar-DZ-IsmaelNeural","ar-EG-SalmaNeural", "ar-EG-ShakirNeural",
    "ar-IQ-RanaNeural", "ar-IQ-BasselNeural","ar-JO-SanaNeural", "ar-JO-TaimNeural",
    "ar-KW-FaresNeural","ar-LB-LaylaNeural", "ar-LB-RamiNeural",
    "ar-LY-ImanNeural", "ar-LY-OmarNeural","ar-MA-MounaNeural", "ar-MA-JamalNeural",
    "ar-OM-SultanNeural","ar-QA-AmalNeural", "ar-QA-MoazNeural",
    "ar-SA-ZariyahNeural", "ar-SA-HamedNeural","ar-SY-AmalNeural", "ar-SY-LaithNeural",
    "ar-TN-ReemNeural", "ar-TN-HediNeural","ar-AE-FatimaNeural", "ar-YE-MaryamNeural",
    "ar-YE-SalehNeural","az-AZ-BanuNeural", "az-AZ-BabekNeural","bg-BG-KalinaNeural",
    "bg-BG-BorislavNeural","bn-BD-NabanitaNeural", "bn-BD-PradeepNeural","bn-IN-BashantiNeural",
    "bn-IN-TapasNeural","bs-BA-VesnaNeural", "bs-BA-GoranNeural","ca-ES-JoanaNeural",
    "ca-ES-EnricNeural","cs-CZ-VlastaNeural", "cs-CZ-AntoninNeural","cy-GB-NiaNeural",
    "cy-GB-AledNeural","da-DK-ChristelNeural", "da-DK-JeppeNeural","de-AT-IngridNeural", 
    "de-AT-JonasNeural","de-CH-KarstenNeural", "de-CH-LinaNeural","de-DE-KatjaNeural", 
    "de-DE-ConradNeural","el-GR-AthinaNeural", "el-GR-NestorasNeural","en-AU-NatashaNeural", 
    "en-AU-WilliamNeural","zh-TW-YunJheNeural""en-CA-ClaraNeural", "en-CA-LiamNeural",
    "en-GB-LibbyNeural", "en-GB-RyanNeural","en-GB-SoniaNeural", "en-GB-AbbiNeural",
    "en-IN-NeerjaNeural", "en-IN-PrabhatNeural","en-IE-EmilyNeural", "en-IE-ConnorNeural",
    "en-NZ-MollyNeural", "en-NZ-MitchellNeural","en-PH-BlessicaNeural", "en-PH-JamesNeural",
    "en-US-JennyNeural", "en-US-GuyNeural","en-US-AriaNeural", "en-US-DavisNeural",
    "es-AR-ElenaNeural", "es-AR-TomasNeural","es-CO-GonzaloNeural", "es-CO-ElenaNeural",
    "es-ES-ElviraNeural", "es-ES-AlvaroNeural","es-MX-DaliaNeural", "es-MX-JorgeNeural",
    "es-US-PalomaNeural", "es-US-AlonsoNeural","et-EE-AnuNeural", "et-EE-KarlNeural",
    "fi-FI-NooraNeural", "fi-FI-SelmaNeural","fil-PH-BlessicaNeural", "fil-PH-AngeloNeural",
    "fr-BE-CharlineNeural", "fr-BE-GerardNeural","fr-CA-SylvieNeural", "fr-CA-AntoineNeural",
    "fr-FR-DeniseNeural", "fr-FR-HenriNeural","fr-CH-FannyNeural", "fr-CH-FelixNeural",
    "ga-IE-OrlaNeural", "ga-IE-ColmNeural","gl-ES-SabelaNeural", "gl-ES-RoiNeural",
    "gu-IN-DhwaniNeural", "gu-IN-MadhavNeural","he-IL-HilaNeural", "he-IL-AvriNeural",
    "hi-IN-MadhurNeural", "hi-IN-SwaraNeural","hr-HR-GabrijelaNeural", "hr-HR-SreckoNeural",
    "hu-HU-NoemiNeural", "hu-HU-TamasNeural","id-ID-GadisNeural", "id-ID-FrederikNeural",
    "is-IS-GudrunNeural", "is-IS-GunnarNeural","it-IT-IsabellaNeural", "it-IT-DiegoNeural",
    "ja-JP-NanamiNeural", "ja-JP-KeitaNeural","jv-ID-SitiNeural", "jv-ID-DimasNeural",
    "km-KH-SothidaNeural", "km-KH-RathanakNeural","kn-IN-SapnaNeural", "kn-IN-GaganNeural",
    "ko-KR-SunHiNeural", "ko-KR-InJoonNeural","lo-LA-KeomanyNeural", "lo-LA-SayfonNeural",
    "lt-LT-OnaNeural", "lt-LT-LeonasNeural","lv-LV-EveritaNeural", "lv-LV-NilsNeural",
    "ml-IN-SobhanaNeural", "ml-IN-MidhunNeural","mr-IN-AarohiNeural", "mr-IN-ManoharNeural",
    "ms-MY-YasminNeural", "ms-MY-OsmanNeural","nb-NO-PernilleNeural", "nb-NO-FinnNeural",
    "ne-NP-SushilaNeural", "ne-NP-RameshNeural","nl-BE-DenaNeural", "nl-BE-ArnaudNeural",
    "nl-NL-ColetteNeural", "nl-NL-FennaNeural","pl-PL-AgnieszkaNeural", "pl-PL-MarekNeural",
    "pt-BR-FranciscaNeural", "pt-BR-AntonioNeural","pt-PT-RaquelNeural", "pt-PT-DuarteNeural",
    "ru-RU-DariyaNeural", "ru-RU-DmitryNeural","sk-SK-ViktoriaNeural", "sk-SK-LukasNeural",
    "sl-SI-PetraNeural", "sl-SI-RokNeural","sv-SE-SofieNeural", "sv-SE-MattiasNeural",
    "ta-IN-PallaviNeural", "ta-IN-ValluvarNeural","te-IN-ShrutiNeural", "te-IN-MohanNeural",
    "th-TH-NatashaNeural", "th-TH-PattaraNeural","tr-TR-EmelNeural", "tr-TR-AhmetNeural",
    "uk-UA-PolinaNeural", "uk-UA-OstapNeural","ur-PK-UzmaNeural", "ur-PK-AsadNeural",
    "vi-VN-HoaiMyNeural", "vi-VN-NamMinhNeural","zh-CN-XiaoxiaoNeural", "zh-CN-YunxiNeural",
    "zh-HK-HiuMaanNeural", "zh-HK-WanLungNeural","zh-TW-HsiaoChenNeural", 
]


TEXT = "hello how are you brother"
# 2nd, is for female
# 3rd are for male
VOICE = VOICES[27]
OUTPUT_FILE = "test_speed.mp3"

async def amain() -> None:
    communicator = edge_tts.Communicate(TEXT, VOICE)
    await communicator.save(OUTPUT_FILE)

    pygame.mixer.init()  # Initialize pygame mixer
    pygame.mixer.music.load(OUTPUT_FILE)  # Load the saved audio file
    pygame.mixer.music.play()  # Play the audio

    while pygame.mixer.music.get_busy():  # Wait until the music finishes
        pygame.time.Clock().tick(10)


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

try:
    loop.run_until_complete(amain())
finally:
    loop.close()
