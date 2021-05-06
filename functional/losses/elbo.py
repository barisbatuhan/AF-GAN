from collections import OrderedDict
import torch
from functional.losses.kl_loss import kl_loss
from functional.losses.reconstruction_loss import reconstruction_loss_distributional


def elbo(z,
         x,
         mu_z,
         mu_x,
         logstd_z,
         logstd_x=None,
         kl_loss_weight=1):
    kl_loss_value = kl_loss(z, mu_z, torch.exp(logstd_z))
    reconstruction_loss = -1 * reconstruction_loss_distributional(mu_x, x, logstd_x)
    loss = reconstruction_loss + kl_loss_weight * kl_loss_value
    return OrderedDict(loss=loss,
                       reconstruction_loss=reconstruction_loss,
                       kl_loss=kl_loss_value)
