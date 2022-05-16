Host = ['Host','id']
Experiment = ['Event', 'experimentID', 'experimentDay','repetition']
Environment = ['level1', 'level2', 'level3']
Pathogen = ['name','index']
Sample = ['SampleType', 'index', 'experimentDay', 'experimentHour', 'result']
Gene = ['name']
BodyMass = ['BodyMass', 'index']
Measure = ['hasNumericalValue']
Measurement = ['M', 'index']
SpecificViableCount = ['Quantity', 'index']
Inoculation =['Inoculation','index']
VolumetricViableCount = ['Dose','index']
Antibiotic = ['Antibiotic','name']
PathogenResistence = ['Resistence','index']

linked_classes = {'Measurement': ['Experiment'],'Inoculation':['Experiment']}
