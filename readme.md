# Natural Language processsing with Transformers
## Lewis Tunstall, Leandro von Werra, Thomas Wolf
### Building Language Applicaiton with Hugging Face applications

"""
In short, I thoroughly enjoyed this book, and I’m certain you will too.
Anyone interested in building products with state-of-the-art languageprocessing features needs to read it. It’s packed to the brim with all the right
brain germs!

Aurélien Géron
"""

# pre book materials suggested

1. Hands-On Machine Learning with Scikit-Learn and TensorFlow,
by Aurélien Géron (O’Reilly)
2. Deep Learning for Coders with fastai and PyTorch, by Jeremy
Howard and Sylvain Gugger (O’Reilly)
3. Natural Language Processing with PyTorch, by Delip Rao and
Brian McMahan (O’Reilly)
4. The Hugging Face Course, by the open source team at Hugging
Face

Transformers offers several layers of abstraction for using and training
transformer models. We’ll start with the easy-to-use pipelines that allow us
to pass text examples through the models and investigate the predictions in
just a few lines of code. Then we’ll move on to tokenizers, model classes,
and the Trainer API, which allow us to train models for our own use
cases. Later, we’ll show you how to replace the Trainer with the
Accelerate library, which gives us full control over the training loop and
allows us to train large-scale transformers entirely from scratch!

Fortunately, there are several free online options that
you can use, including:
1. Google Colaboratory
2. Kaggle Notebooks
3. Paperspace Gradient Notebooks

To run the examples, you’ll need to follow the installation guide that we
provide in the book’s GitHub repository. You can find this guide and the
code examples at https://github.com/nlp-with-transformers/notebooks.

## Fine tuning

![](fine_tuning/fine_tuning.png)

## working on bengali translation