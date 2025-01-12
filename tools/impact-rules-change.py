import math

div_solvers_repeated = {
"ABVFP":            0,
"ALIA":             2,
"AUFBVDTLIAn":      0,
"AUFDTLIA":         0,
"AUFLIA":           2,
"AUFLIRA":          2,
"AUFNIA":           1,
"AUFNIRA":          1,
"BV":               1,
"BVFP":             0,
"FP":               0,
"LIA":              2,
"LRA":              2,
"NIA":              1,
"NRA":              1,
"QF_ABV":           1,
"QF_ABVFPn":        0,
"QF_ALIA":          0,
"QF_ANIA":          2,
"QF_AUFBV":         1,
"QF_AUFLIA":        0,
"QF_AUFNIA":        1,
"QF_AX":            0,
"QF_BV":           13,
"QF_BVFP":          0,
"QF_BVFPLRAn":      0,
"QF_DT":            0,
"QF_FP":            0,
"QF_FPLRAn":        0,
"QF_IDL":           0,
"QF_LIA":           0,
"QF_LIRA":          0,
"QF_LRA":           0,
"QF_NIA":           1,
"QF_NIRA":          1,
"QF_NRA":           1,
"QF_RDL":           0,
"QF_Se":            0,
"QF_SLIAe":         0,
"QF_UF":            0,
"QF_UFBV":          0,
"QF_UFIDL":         0,
"QF_UFLIA":         0,
"QF_UFLRA":         0,
"QF_UFNIA":         1,
"QF_UFNRA":         1,
"UF":               2,
"UFBV":             0,
"UFDT":             0,
"UFDTLIA":          0,
"UFDTNIA":          0,
"UFIDL":            2,
"UFLIA":            2,
"UFLRA":            2,
"UFNIA":            1
}

div_solvers = {
"ABVFP":           4,
"ALIA":           10,
"AUFBVDTLIAn":     2,
"AUFDTLIA":        4,
"AUFLIA":         11,
"AUFLIRA":        12,
"AUFNIA":          7,
"AUFNIRA":         8,
"BV":              8,
"BVFP":            4,
"FP":              4,
"LIA":            10,
"LRA":             9,
"NIA":             7,
"NRA":             8,
"QF_ABV":          7,
"QF_ABVFPn":       3,
"QF_ALIA":         7,
"QF_ANIA":         6,
"QF_AUFBV":        6,
"QF_AUFLIA":       7,
"QF_AUFNIA":       6,
"QF_AX":           6,
"QF_BV":          24,
"QF_BVFP":         4,
"QF_BVFPLRAn":     2,
"QF_DT":           3,
"QF_FP":           5,
"QF_FPLRAn":       2,
"QF_IDL":          8,
"QF_LIA":         11,
"QF_LIRA":         6,
"QF_LRA":         11,
"QF_NIA":         11,
"QF_NIRA":         7,
"QF_NRA":         11,
"QF_RDL":          6,
"QF_Se":           1,
"QF_SLIAe":        2,
"QF_UF":           9,
"QF_UFBV":         6,
"QF_UFIDL":        6,
"QF_UFLIA":        7,
"QF_UFLRA":        7,
"QF_UFNIA":        7,
"QF_UFNRA":        9,
"UF":             12,
"UFBV":            5,
"UFDT":            4,
"UFDTLIA":         4,
"UFDTNIA":         3,
"UFIDL":          10,
"UFLIA":          11,
"UFLRA":          10,
"UFNIA":          10
}

# after removing commonly solved in 1s
div_benchs = {
"ABVFP":            1,
"ALIA":            19,
"AUFBVDTLIAn":    854,
"AUFDTLIA":       275,
"AUFLIA":        1638,
"AUFLIRA":       1683,
"AUFNIA":           3,
"AUFNIRA":        300,
"BV":             823,
"BVFP":            24,
"FP":            1238,
"LIA":            300,
"LRA":           1003,
"NIA":             11,
"NRA":             93,
"QF_ABV":        7538,
"QF_ABVFPn":      630,
"QF_ALIA":        139,
"QF_ANIA":          7,
"QF_AUFBV":        41,
"QF_AUFLIA":      651,
"QF_AUFNIA":        9,
"QF_AX":          300,
"QF_BV":         8909,
"QF_BVFP":        516,
"QF_BVFPLRAn":      1,
"QF_DT":            4,
"QF_FP":          250,
"QF_FPLRAn":       13,
"QF_IDL":        1042,
"QF_LIA":        3136,
"QF_LIRA":          7,
"QF_LRA":         546,
"QF_NIA":       11494,
"QF_NIRA":          2,
"QF_NRA":        2842,
"QF_RDL":         247,
"QF_Se":          988,
"QF_SLIAe":     23175,
"QF_UF":         3512,
"QF_UFBV":        223,
"QF_UFIDL":       300,
"QF_UFLIA":       300,
"QF_UFLRA":       541,
"QF_UFNIA":       300,
"QF_UFNRA":        26,
"UF":            2816,
"UFBV":            72,
"UFDT":          1547,
"UFDTLIA":        299,
"UFDTNIA":          1,
"UFIDL":           20,
"UFLIA":         2848,
"UFLRA":            7,
"UFNIA":         6253
}

if __name__ == '__main__':
  old_jobs = 0
  new_jobs = 0
  new_jobs_newperc = 0
  new_jobs_norep = 0
  for div, benchs in div_benchs.items():
    new_benchs = int(math.ceil(benchs * 0.8 if benchs > 300 else benchs))
    old_jobs += benchs*div_solvers[div]
    new_jobs_norep += benchs*(div_solvers[div] - div_solvers_repeated[div])
    new_jobs_newperc += new_benchs*div_solvers[div]
    new_jobs += new_benchs*(div_solvers[div] - div_solvers_repeated[div])

  print("Old jobs " + str(old_jobs))
  print("New jobs (no repeated) " + str(new_jobs_norep) + " [{0:.0f}%]".format((new_jobs_norep/old_jobs)*100))
  print("New jobs (new percentage) " + str(new_jobs_newperc) + " [{0:.0f}%]".format((new_jobs_newperc/old_jobs)*100))
  print("New jobs (both) " + str(new_jobs) + " [{0:.0f}%]".format((new_jobs/old_jobs)*100))
