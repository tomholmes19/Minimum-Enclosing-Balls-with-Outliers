import data.generation, data.loading

test_data = data.generation.normal(0,1,1000,5)
data.loading.to_csv(test_data, "src/test/normal_test.csv")