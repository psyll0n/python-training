class One:
    def speak(self):
        print("This is #1")

    def total_tacos(self):
        return 5


class Two(One):
    def speak(self):
        super().speak()
        print("This is #2")

    def total_tacos(self):
        total_original_tacos = super().total_tacos()
        print("Original tacos: ", total_original_tacos)
        new_tacos = total_original_tacos + 3
        print("New total tacos: ", new_tacos)
        return new_tacos


two = Two()
two.speak()

two.total_tacos()
