# Hyper params : num_hidden, learning rate, epochs, num_timesteps
import random


class geneticStuffs:
    # learning_rate_dict = {0: 0.01, 1: 0.001, 2: 0.0001}
    # num_hidden_dict = {0: 64, 1: 128, 2: 256}
    # epochs_dict = {0: 30, 1: 50, 2: 70}
    # timesteps_dict = {0:20, 1:50, 2: 70}
    # 9 = 511, 10=1023 ,4 = 15 , 9 = 511

    gene_num_bits = [10,9,4,9]

    chromosome_length = sum(gene_num_bits)

    num_hyper_parameters = 4
    num_population = 20
    max_generations = 70

    mutation_probability = 0.3

    def __init__(self):
        self.gene = [random.randint(0,1) for i in range(self.chromosome_length)]
        self.fitness = None
        self.phenoType = []
        self.convert_to_phenotype()

    def convert_to_phenotype(self):
        self.phenoType = []
        boundary = 0
        for each in self.gene_num_bits:
            self.phenoType.append(int(''.join(map(str,self.gene[boundary:boundary+each])),2))
            boundary += each

    def convert_to_genotype(self):
        # will only use when next iteration due to lack of RAm in google colab
        # transforms phenoType to genotype

        gene = []
        for i, hyper in enumerate(self.phenoType):
            binary_ = '{0:0' + str(self.gene_num_bits[i]) + 'b}'
            gene.extend(list(binary_.format(hyper)))
        gene = [int(each) for each in gene]
        self.gene = gene

    def crossover(self, model_1,model_2,crossover_point):
        self.gene = model_1.gene[:crossover_point] + model_2.gene[crossover_point:]
        self.convert_to_phenotype()

    def mutate(self):
        boundary = 0
        change_points = []
        for each in self.gene_num_bits:
            change_points.append(random.randint(boundary,boundary+each-1))
            boundary += each
        for change_point in change_points:
            self.gene[change_point] = 1 - self.gene[change_point]
        self.convert_to_phenotype()

    def set_fitness(self, fitness_value):
        self.fitness = fitness_value
