import re

# Dictionary of translations for summary definitions
# Keys are the exact English strings found in summary files
translations_map = {
    # --- Atomic Structure ---
    "Proton": "质子",
    ": A positively charged subatomic particle found in the nucleus; defines the element (atomic number).": "：发现于原子核中的带正电荷的亚原子粒子；定义了元素（原子序数）。",
    "Neutron": "中子",
    ": A neutral subatomic particle found in the nucleus; contributes to atomic mass.": "：发现于原子核中的中性亚原子粒子；有助于原子质量。",
    "Electron": "电子",
    ": A negatively charged particle orbiting the nucleus in energy levels; very small mass.": "：在能级中绕原子核运行的带负电粒子；质量非常小。",
    "Atomic Number": "原子序数",
    ": The number of protons in an atom; identifies the element.": "：原子中质子的数量；识别元素。",
    "Mass Number": "质量数",
    ": The total number of protons + neutrons in the nucleus.": "：原子核中质子 + 中子的总数。",
    "Charge Balance": "电荷平衡",
    ": In a neutral atom, the number of protons equals the number of electrons.": "：在中性原子中，质子数等于电子数。",
    "Nucleus": "原子核",
    ": The dense, central core of an atom containing protons and neutrons.": "：包含质子和中子的原子致密切核心。",
    "Isotope": "同位素",
    ": Atoms of the same element with different numbers of neutrons (same protons, different mass numbers).": "：具有不同中子数的同种元素原子（质子数相同，质量数不同）。",
    "Atomic Mass": "原子质量",
    ": The weighted average mass of all naturally occurring isotopes of an element.": "：元素所有天然同位素的加权平均质量。",
    
    # --- Models ---
    "Dalton's Atomic Theory": "道尔顿原子理论",
    ": All matter is made of atoms; atoms of the same element are identical; atoms combine in whole-number ratios.": "：所有物质都由原子构成；同种元素的原子是相同的；原子以整数比结合。",
    "Thomson's Model": "汤姆逊模型",
    ": Discovered the electron; proposed the 'plum pudding' model with negative charges in positive mass.": "：发现了电子；提出了带负电荷镶嵌在正电荷物质中的'葡萄干布丁'模型。",
    "Rutherford's Model": "卢瑟福模型",
    ": Discovered the nucleus through the gold foil experiment; most of the atom is empty space.": "：通过金箔实验发现了原子核；原子大部分是空的空间。",
    "Bohr's Model": "玻尔模型",
    ": Electrons orbit the nucleus in fixed energy levels (like planets around the sun).": "：电子在固定的能级轨道上绕核运行（像行星绕太阳一样）。",
    "Modern Model": "现代模型",
    ": The quantum mechanical model; electrons exist in probability clouds (orbitals), not fixed paths.": "：量子力学模型；电子存在于概率云（轨道）中，而不是固定路径。",
    
    # --- Electrons & Orbitals ---
    "Electron Cloud": "电子云",
    ": The region around the nucleus where electrons are most likely to be found.": "：原子核周围最可能找到电子的区域。",
    "Energy Levels": "能级",
    ": Regions around the nucleus where electrons orbit; numbered 1, 2, 3, etc.": "：原子核周围电子运行的区域；编号为 1, 2, 3 等。",
    "Orbital": "轨道",
    ": A region of space where there is a high probability of finding an electron.": "：空间中发现电子概率很高的区域。",
    "s Orbital": "s 轨道",
    ": Spherical-shaped orbital; each energy level has one s orbital (holds 2 electrons).": "：球形轨道；每个能级有一个 s 轨道（容纳 2 个电子）。",
    "p Orbital": "p 轨道",
    ": Dumbbell-shaped orbital; exists starting from the 2nd energy level (3 orbitals, holds 6 electrons).": "：哑铃形轨道；从第 2 能级开始存在（3 个轨道，容纳 6 个电子）。",
    "d Orbital": "d 轨道",
    ": Clover-shaped orbital; exists starting from the 3rd energy level (5 orbitals, holds 10 electrons).": "：三叶草形轨道；从第 3 能级开始存在（5 个轨道，容纳 10 个电子）。",
    "Electron Configuration": "电子排布",
    ": The arrangement of electrons in an atom's orbitals (e.g., 1s² 2s² 2p⁶).": "：原子轨道中电子的排列（例如 1s² 2s² 2p⁶）。",
    "Valence Electrons": "价电子",
    ": Electrons in the outermost energy level; determine an element's chemical behavior.": "：最外层能级中的电子；决定元素的化学行为。",
    "Octet Rule": "八隅体规则",
    ": Atoms tend to gain, lose, or share electrons to have 8 valence electrons (stable).": "：原子倾向于获得、失去或共享电子以拥有 8 个价电子（稳定）。",
    
    # --- Periodic Table ---
    "Periodic Table": "元素周期表",
    ": The organized chart listing all known elements with their symbols, atomic numbers, and masses.": "：列出所有已知元素及其符号、原子序数和质量的有组织图表。",
    "Periods": "周期",
    ": Horizontal rows on the periodic table; elements in the same period have the same number of energy levels.": "：周期表上的横行；同一周期的元素具有相同数量的能级。",
    "Groups/Families": "族",
    ": Vertical columns; elements in the same group have similar chemical properties and the same number of valence electrons.": "：纵列；同一族的元素具有相似的化学性质和相同数量的价电子。",
    "Metals": "金属",
    ": Found on the left side; good conductors, malleable, ductile, shiny.": "：位于左侧；良导体，有延展性，有光泽。",
    "Nonmetals": "非金属",
    ": Found on the right side; poor conductors, brittle as solids, dull.": "：位于右侧；不良导体，固体易碎，无光泽。",
    "Metalloids": "类金属",
    ": Found along the staircase line; have properties of both metals and nonmetals (e.g., silicon).": "：位于阶梯线上；具有金属和非金属的性质（例如硅）。",
    "Alkali Metals (Group 1)": "碱金属 (第 1 族)",
    ": Have 1 valence electron; very reactive, easily lose 1 electron.": "：有 1 个价电子；非常活泼，容易失去 1 个电子。",
    "Halogens (Group 17)": "卤素 (第 17 族)",
    ": Have 7 valence electrons; very reactive, easily gain 1 electron.": "：有 7 个价电子；非常活泼，容易获得 1 个电子。",
    "Noble Gases (Group 18)": "稀有气体 (第 18 族)",
    ": Have 8 valence electrons (full outer shell); very stable and unreactive.": "：有 8 个价电子（满外壳）；非常稳定且不活泼。",
    
    # --- Trends ---
    "Atomic Radius": "原子半径",
    ": Increases going DOWN a group (more energy levels) and DECREASES going across a period (more protons pull electrons closer).": "：沿族向下增加（更多能级），沿周期向右减小（更多质子将电子拉得更近）。",
    "Ionization Energy": "电离能",
    ": The energy required to remove an electron; INCREASES across a period and DECREASES down a group.": "：移除电子所需的能量；沿周期向右增加，沿族向下减小。",
    "Electronegativity": "电负性",
    ": An atom's ability to attract electrons in a bond; INCREASES across a period and DECREASES down a group.": "：原子在键中吸引电子的能力；沿周期向右增加，沿族向下减小。",
    "Shielding Effect": "屏蔽效应",
    ": Inner electrons block (shield) outer electrons from the full nuclear charge.": "：内层电子阻挡（屏蔽）外层电子受到完整的核电荷吸引。",
    
    # --- Bonding ---
    "Ionic Bonds": "离子键",
    ": Ionic bonds involve _______ of electrons.": "：离子键涉及电子的 _______。",
    ": Transfer": "：转移",
    ": Ionic bonds occur between": "：离子键发生在",
    ": Metal and Nonmetal": "：金属和非金属之间",
    "Covalent Bonds": "共价键",
    ": Covalent bonds involve _______ of electrons.": "：共价键涉及电子的 _______。",
    ": Sharing": "：共享",
    ": Covalent bonds occur between": "：共价键发生在",
    ": Nonmetal and Nonmetal": "：非金属和非金属之间",
    "Metallic Bonds": "金属键",
    ": Describe metallic bonding.": "：描述金属键合。",
    ": Sea of electrons": "：电子海",
    "VSEPR Theory": "VSEPR 理论",
    ": Valence Shell Electron Pair Repulsion — electron pairs around a central atom arrange to minimize repulsion.": "：价层电子对互斥——中心原子周围的电子对排列以最小化排斥。",
    
    # --- Naming ---
    "Prefix for 1": "1 的前缀",
    ": Mono-": "：Mono- (单-)",
    "Prefix for 2": "2 的前缀",
    ": Di-": "：Di- (二-)",
    "Prefix for 3": "3 的前缀",
    ": Tri-": "：Tri- (三-)",
    "Prefix for 4": "4 的前缀",
    ": Tetra-": "：Tetra- (四-)",
    
    # --- Reactions ---
    "Chemical Equilibrium": "化学平衡",
    ": A state where the forward and reverse reaction rates are equal; concentrations remain constant.": "：正向和逆向反应速率相等的状态；浓度保持恒定。",
    "Le Chatelier's Principle": "勒夏特列原理",
    ": If a stress is applied to a system at equilibrium, the system shifts to relieve the stress.": "：如果对平衡系统施加压力，系统会移动以减轻压力。",
    "Activation Energy (Ea)": "活化能 (Ea)",
    ": The minimum energy required for a chemical reaction to begin.": "：化学反应开始所需的最小能量。",
    "Catalyst": "催化剂",
    ": A substance that lowers activation energy without being consumed in the reaction.": "：降低活化能且在反应中不被消耗的物质。",
    "Endothermic Reaction": "吸热反应",
    ": Products have more energy than reactants; energy is absorbed.": "：生成物的能量高于反应物；能量被吸收。",
    "Exothermic Reaction": "放热反应",
    ": Products have less energy than reactants; energy is released.": "：生成物的能量低于反应物；能量被释放。",
    
    # --- Stoichiometry & Gases ---
    "Stoichiometry": "化学计量",
    ": The calculation of quantities in chemical reactions using mole ratios from balanced equations.": "：利用平衡方程中的摩尔比计算化学反应中的量。",
    "Mole": "摩尔",
    ": The SI unit for amount of substance; 1 mole = 6.022 × 10²³ particles.": "：物质的量的 SI 单位；1 摩尔 = 6.022 × 10²³ 个粒子。",
    "Avogadro's Number": "阿伏伽德罗常数",
    ": 6.022 × 10²³ — the number of particles (atoms, molecules, ions) in one mole.": "：6.022 × 10²³ — 1 摩尔中的粒子（原子、分子、离子）数量。",
    "Ideal Gas Law": "理想气体定律",
    ": PV = nRT; relates pressure, volume, moles, and temperature.": "：PV = nRT；通过压力、体积、摩尔和温度相关联。",
    "Boyle's Law": "玻意耳定律",
    ": At constant temperature, pressure and volume are inversely proportional: P₁V₁ = P₂V₂.": "：恒温下，压力与体积成反比：P₁V₁ = P₂V₂。",
    "Charles' Law": "查理定律",
    ": At constant pressure, volume and temperature are directly proportional: V₁/T₁ = V₂/T₂.": "：恒压下，体积与温度成正比：V₁/T₁ = V₂/T₂。",
    
    # --- Solutions ---
    "Solution": "溶液",
    ": A homogeneous mixture where the solute is evenly distributed in the solvent.": "：溶质均匀分布在溶剂中的均匀混合物。",
    "Solute": "溶质",
    ": The substance that is dissolved in the solution (usually present in smaller amount).": "：溶解在溶液中的物质（通常量较少）。",
    "Solvent": "溶剂",
    ": The substance that does the dissolving (usually present in larger amount).": "：起溶解作用的物质（通常量较多）。",
    "Molarity (M)": "摩尔浓度 (M)",
    ": The number of moles of solute per liter of solution. M = mol / L.": "：每升溶液中溶质的摩尔数。M = mol / L。",
    "Diffusions": "扩散",
    "Saturated Solution": "饱和溶液",
    ": Contains the maximum amount of dissolved solute at a given temperature.": "：在给定温度下包含最大溶解溶质的量。",
    
    # --- Acids & Bases ---
    "Acid": "酸",
    ": A substance that produces H⁺ (hydrogen) ions in solution; tastes sour; pH below 7.": "：在溶液中产生 H⁺（氢）离子的物质；味酸；pH 值低于 7。",
    "Base": "碱",
    ": A substance that produces OH⁻ (hydroxide) ions in solution; tastes bitter, feels slippery; pH above 7.": "：在溶液中产生 OH⁻（氢氧根）离子的物质；味苦，有滑腻感；pH 值高于 7。",
    "pH Scale": "pH 标度",
    ": Measures hydrogen ion concentration; ranges from 0 (most acidic) to 14 (most basic); 7 is neutral.": "：测量氢离子浓度；范围从 0（最酸）到 14（最碱）；7 为中性。",
    "Titration": "滴定",
    ": A lab technique to determine the concentration of an acid or base using a neutralization reaction.": "：利用中和反应测定酸或碱浓度的实验室技术。",
    
    # --- Nuclear ---
    "Radioactivity": "放射性",
    ": The spontaneous emission of radiation from an unstable nucleus.": "：不稳定原子核自发发射辐射。",
    "Alpha Decay": "Alpha 衰变",
    ": Emission of an alpha particle (²₄He); reduces atomic number by 2 and mass number by 4.": "：发射 Alpha 粒子 (²₄He)；原子序数减少 2，质量数减少 4。",
    "Beta Decay": "Beta 衰变",
    ": A neutron converts to a proton and emits a beta particle (electron); atomic number increases by 1.": "：中子转化为质子并发射 Beta 粒子（电子）；原子序数增加 1。",
    "Gamma Radiation": "Gamma 辐射",
    ": High-energy electromagnetic radiation emitted from the nucleus; no change in mass or atomic number.": "：原子核发射的高能电磁辐射；质量或原子序数无变化。",
    "Half-Life (t½)": "半衰期",
    ": The time it takes for half of a radioactive sample to decay.": "：放射性样本衰变一半所需的时间。",
    "Fission": "裂变",
    "Fusion": "聚变",
    ": The splitting of a heavy nucleus into two lighter nuclei, releasing large amounts of energy.": "：重原子核分裂成两个较轻的原子核，释放大量能量。",
    ": The combining of two light nuclei into one heavier nucleus, releasing even more energy.": "：两个轻原子核结合成一个较重的原子核，释放更多能量。",
    
    # --- Specific Keys from Definitions File ---
    ": A change that does not alter the composition of the substance": "：不改变物质组成的得变化",
    ": A change that produces new substances": "：产生新物质的变化",
    ": Loss of electrons": "：失去电子",
    ": Gain of electrons": "：获得电子",
    ": OIL RIG": "：OIL RIG (氧化是失去，还原是获得)",
    ": Energy transfer due to temperature difference": "：由于温度差异而产生的能量传递",
    ": Disorder or randomness": "：无序或随机性",
    ": Spontaneity": "：自发性",
    ": Spontaneous reaction": "：自发反应",
    ": Electrons in the outermost energy level": "：最外层能级中的电子",
    ": To achieve a stable octet (8 valence electrons)": "：达到稳定的八隅体（8 个价电子）",
    ": A reaction that releases heat/energy to the surroundings": "：向环境释放热/能量的反应",
    ": A reaction that absorbs heat/energy from the surroundings": "：从环境吸收热/能量的反应",
    ": Depend on number of solute particles, not identity": "：取决于溶质粒子的数量，而不是身份",
    ": Adding solute lowers freezing point": "：加入溶质降低凝固点",
    ": Adding solute raises boiling point": "：加入溶质升高沸点",
    ": Adding solute lowers vapor pressure": "：加入溶质降低蒸气压",
    ": Mass of one mole of a substance": "：一摩尔物质的质量",
    ": Solution that resists pH change": "：抵抗 pH 变化的溶液",
    ": Reducing concentration by adding solvent": "：通过添加溶剂降低浓度",
    ": Gas particles are small, hard spheres with insignificant volume": "：气体粒子是体积可忽略不计的小硬球",
    ": Motion is rapid, constant, and random": "：运动是快速、恒定和随机的",
    ": Collisions are perfectly elastic": "：碰撞是完全弹性的",
    ": Collisions of particles with container walls": "：粒子与容器壁的碰撞",
    ": A state where the forward and reverse reaction rates are equal; concentrations remain constant.": "：正向和逆向反应速率相等的状态；浓度保持恒定。",
    
    # Unit Conversions & Measurement
    ": A method of converting units using conversion factors to cancel unwanted units.": "：使用换算因子来抵消不需要的单位的单位换算方法。",
    ": A ratio equal to 1 that relates two different units (e.g., 1 km / 1000 m).": "：等于 1 的比率，关联两个不同的单位（例如 1 km / 1000 m）。",
    ": Place the given unit in a position to cancel, and the desired unit in the answer position.": "：将给定单位放在抵消位置，将所需单位放在答案位置。",
    ": The final answer must have the correct desired unit to verify the conversion.": "：最终答案必须具有正确的所需单位以验证换算。",
    ": The digits in a measurement that are known with certainty plus one estimated digit.": "：测量中已知确定的数字加上一位估计数字。",
    ": All non-zero digits are always significant (e.g., 123 has 3 sig figs).": "：所有非零数字总是有效的（例如 123 有 3 个有效数字）。",
    ": Zeros between non-zero digits are significant (e.g., 1002 has 4 sig figs).": "：非零数字之间的零是有效的（例如 1002 有 4 个有效数字）。",
    ": Zeros before the first non-zero digit are NOT significant (e.g., 0.0045 has 2 sig figs).": "：第一个非零数字之前的零无效（例如 0.0045 有 2 个有效数字）。",
    ": Zeros at the end of a number are significant only if there is a decimal point (e.g., 100. has 3 sig figs).": "：只有当有小数点时，数字末尾的零才有效（例如 100. 有 3 个有效数字）。",
    ": A way to express very large or very small numbers as a × 10ⁿ, where 1 ≤ a < 10.": "：一种将非常大或非常小的数字表示为 a × 10ⁿ 的方法，其中 1 ≤ a < 10。",
    ": The power of 10 that indicates how many places the decimal moves.": "：表示小数点移动位数的 10 的幂。",
    ": Indicates a large number; decimal moves to the right (e.g., 3.0 × 10³ = 3000).": "：表示大数；小数点向右移动（例如 3.0 × 10³ = 3000）。",
    ": Indicates a small number; decimal moves to the left (e.g., 2.5 × 10⁻² = 0.025).": "：表示小数；小数点向左移动（例如 2.5 × 10⁻² = 0.025）。",
    ": Writing a number without scientific notation (e.g., 45000 instead of 4.5 × 10⁴).": "：不使用科学计数法书写数字（例如 45000 而不是 4.5 × 10⁴）。",
    
    # Specific QA
    ": 1 cm^3": "：1 cm^3",
    ": Sodium Chloride": "：氯化钠",
    ": Magnesium Oxide": "：氧化镁",
    ": Nitrate": "：硝酸根",
    ": Sulfate": "：硫酸根",
    ": Hydroxide": "：氢氧根",
    ": Ammonium": "：铵根",
    ": Phosphate": "：磷酸根",
    ": Crystal Lattice": "：晶格",
    ": When melted or dissolved (electrolyte)": "：熔化或溶解时（电解质）",
    ": Completely dissociates (ionizes) in water. Examples: HCl, HNO₃, H₂SO₄.": "：在水中完全解离（电离）。例如：HCl, HNO₃, H₂SO₄。",
    ": Only partially dissociates in water; establishes equilibrium. Example: CH₃COOH (acetic acid).": "：在水中仅部分解离；建立平衡。例如：CH₃COOH（乙酸）。",
    ": Completely dissociates in water. Examples: NaOH, KOH, Ca(OH)₂.": "：在水中完全解离。例如：NaOH, KOH, Ca(OH)₂。",
    ": Only partially dissociates in water. Example: NH₃ (ammonia).": "：在水中仅部分解离。例如：NH₃（氨）。",
    ": Use the prefix \"hydro-\" + root of the element + \"-ic acid\" (e.g., hydrochloric acid).": "：使用前缀 \"hydro-\" + 元素词根 + \"-ic acid\"（例如：盐酸）。",
    ": If the polyatomic ion ends in \"-ate,\" the acid ends in \"-ic acid\"; if \"-ite,\" then \"-ous acid.\"": "：如果多原子离子以 \"-ate\" 结尾，酸以 \"-ic acid\" 结尾；如果是 \"-ite\"，则是 \"-ous acid\"。",
    ": pH < 7 (high [H⁺], low [OH⁻]).": "：pH < 7（高 [H⁺]，低 [OH⁻]）。",
    ": pH > 7 (low [H⁺], high [OH⁻]).": "：pH > 7（低 [H⁺]，高 [OH⁻]）。",
    ": Chemicals that change color depending on pH (e.g., litmus, phenolphthalein).": "：随 pH 改变颜色的化学品（例如石蕊，酚酞）。",
    ": hydro- + element root + -ic acid. Example: HBr → hydrobromic acid.": "：hydro- + 元素词根 + -ic acid。例如：HBr → 氢溴酸。",
    ": Drop \"-ate,\" add \"-ic acid.\" Example: H₂SO₄ (sulfate → sulfuric acid).": "：去掉 \"-ate,\" 加上 \"-ic acid.\" 例如：H₂SO₄（硫酸根 → 硫酸）。",
    ": Drop \"-ite,\" add \"-ous acid.\" Example: H₂SO₃ (sulfite → sulfurous acid).": "：去掉 \"-ite,\" 加上 \"-ous acid.\" 例如：H₂SO₃（亚硫酸根 → 亚硫酸）。"
}

# Load existing content
json_path = "../ArisEdu Project Folder/scripts/global_translations.js"
with open(json_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Build injection string
insertion = ""
for key, val in translations_map.items():
    # Helper to check if string exists in file loosely to avoid duplication
    # We escape double quotes for the content check since they are in JSON
    json_key_str = f'"{key}"'
    if json_key_str not in content:
        # Escape characters for JSON
        safe_key = key.replace('"', '\\"').replace('\n', ' ')
        safe_val = val.replace('"', '\\"').replace('\n', ' ')
        insertion += f'  "{safe_key}": "{safe_val}",\n'

if insertion:
    # Use the same anchor mechanism
    anchor = '"IN PROGRESS": "进行中"'
    if anchor in content:
        replacement = f'{anchor},\n{insertion.rstrip(",\n")}'
        new_content = content.replace(anchor, replacement)
        with open(json_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Successfully injected {len([l for l in insertion.splitlines() if l])} summary definitions.")
    else:
        print("Anchor not found.")
else:
    print("No new unique Summary definitions to inject.")
