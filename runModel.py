
from utilityFunctions import detect_language
from trainModel import trainModel
profiles = trainModel()


test_text = """
(NARR)  Una nieta habla con su abuelo

(WA) ¡Ay, abuelito, ya no puedo más! Estoy cansada de estudiar tanto. Parece que mientras más estudio en mi curso de tecnología electrónica, más me queda por aprender.

(MA) En cierto modo la vida parecía más sencilla cuando no teníamos tanta información a nuestra disposición. Pero la tecnología moderna nos puede ayudar a mejorar las pésimas condiciones que hay en muchos países del mundo, ¿no te parece?

(WA)  Por supuesto, pero tengo que aprender tanto antes de poder dedicarme a estos problemas. Además, me preocupa que la modernización resulte en una pérdida de sensibilidad humana.

(MA) Hija mía, el que eso te preocupe es buena señal de que tú, por lo menos, no vas a permitir que eso ocurra. Y ahora háblame un poco de esa nueva computadora que anuncian tanto en la tele.
"""

result = detect_language(test_text, profiles)
print(f"Detected language: {result}")