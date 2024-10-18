import matplotlib.pyplot as plt

# 중수소-삼중수소 반응에서 방출되는 에너지 (MeV)
energy_per_reaction_mev = 17.6
# 1 MeV = 1.60218e-13 J
energy_per_reaction_joules = energy_per_reaction_mev * 1.60218e-13

# 중수소와 삼중수소의 몰 질량 (g/mol)
deuterium_molar_mass = 2.014
tritium_molar_mass = 3.016

def calculate_energy_output(hydrogen_mass_kg):
    # 1:1 비율로 중수소와 삼중수소가 섞여 있다고 가정
    deuterium_mass_kg = hydrogen_mass_kg / 2
    tritium_mass_kg = hydrogen_mass_kg / 2
    
    # 중수소와 삼중수소의 몰수 계산
    deuterium_moles = deuterium_mass_kg * 1000 / deuterium_molar_mass
    tritium_moles = tritium_mass_kg * 1000 / tritium_molar_mass
    
    # 반응 횟수 계산 (최소값을 사용)
    avogadro_number = 6.022e23
    reactions = min(deuterium_moles, tritium_moles) * avogadro_number
    
    # 총 에너지 계산 (Joules)
    total_energy_output_joules = reactions * energy_per_reaction_joules
    # J를 KJ로 변환
    total_energy_output_kj = total_energy_output_joules / 1000
    
    return total_energy_output_kj

# 수소의 양 (kg)을 증가시키며 에너지 출력 계산
hydrogen_masses = [i * 0.1 for i in range(1, 1001)]
energy_outputs_kj = [calculate_energy_output(mass) for mass in hydrogen_masses]

# 사용자 입력 받기
user_input = float(input("Enter the amount of hydrogen (in kg): "))
user_energy_output_kj = calculate_energy_output(user_input)

# 결과를 시각화
plt.figure(figsize=(10, 6))
plt.plot(hydrogen_masses, energy_outputs_kj, label='Energy Output')
plt.scatter([user_input], [user_energy_output_kj], color='red', zorder=5, label=f'User Input: {user_input} kg, Output: {user_energy_output_kj} kj')
plt.xlabel('Hydrogen Mass (kg)')
plt.ylabel('Energy Output (kJ)')
plt.title('Energy Output from Hydrogen Fusion')
plt.legend()
plt.grid(True)
plt.show()
print(user_energy_output_kj)