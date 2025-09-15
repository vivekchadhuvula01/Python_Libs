import tensorflow as tf
import keras
import numpy
# print("Tensorflow Version: ",tf.__version__)

'''
Load and prepare the MNIST dataset. The pixel values of the images range from 0 through 255. Scale these values to a range of 0 to 1 by dividing the values by 255.0. This also converts the sample data from integers to floating-point numbers:
'''
mnist = keras.datasets.mnist

(x_train,y_train) , (x_test,y_test) = mnist.load_data()

x_train, x_test = x_train/255.0 , x_test/255.0

'''
Build a Machine Learning Model
'''

model = keras.models.Sequential([
    keras.layers.Flatten(input_shape = (28,28)),
    keras.layers.Dense(128,activation='relu'),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(10)
])

predictions = model(x_train[:1]).numpy()
# print(predictions)
tf.nn.softmax(predictions).numpy()

loss_fn = keras.losses.SparseCategoricalCrossentropy(from_logits=True)
loss_fn(y_train[:1], predictions).numpy()

# print(loss_fn)

model.compile(optimizer='admin',
              loss=loss_fn,
              metrics=['accuracy'])

model.fit(x_train,y_train,epochs=5)

model.evaluate(x_test,y_test,verbose=2)


probability_model = keras.Sequential([
    model,
    keras.layers.Softmax()
])

probability_model(x_test[:5])
print(probability_model)