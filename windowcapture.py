while True:

    # TESTE DE ÁUDIO AQUI
    print("Testando áudio dentro do while do YOLO...")
    voz.say("Teste dentro do YOLO")
    voz.runAndWait()

    # YOLO roda aqui
    result = modelo.predict(source="0", show=True)

    time.sleep(2)