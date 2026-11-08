from varasto import Varasto


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")

    print("Lisätään 50.7 ja otetaan 3.14")
    mehua.lisaa_varastoon(50.7)
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")
    print("Tämä ylimääräinen rivi rikkoo max-statements (11/10) ja max-line-length (88/80) -säännöt!")


if __name__ == "__main__":
    main()
