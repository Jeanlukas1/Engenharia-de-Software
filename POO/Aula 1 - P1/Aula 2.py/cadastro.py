import banco

ze = banco.Banco("Saqua Eng Software", 1, 1, "Zé da manga", "123456789-00")

zecove = banco.Banco("Inter", 1, 1006, "Zé das coves", "00987465123")

print(ze)

print(zecove)

zecove.definir_senha("12345")

ze.definir_senha("admin01")

ze.deposito(5000)

ze.pix(zecove, 2000)

ze.saque("admin01", 1000)

ze.extrato()

zecove.extrato()

