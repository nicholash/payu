# coding: utf-8

from payu.experiment import Experiment
from payu.laboratory import Laboratory
import payu.subcommands.args as args

title = 'setup'
parameters = {'description': 'Setup model work directory for run'}

arguments = [args.model, args.config, args.laboratory, args.force_archive]


def runcmd(model_type, config_path, lab_path, force_archive):

    lab = Laboratory(model_type, config_path, lab_path)
    expt = Experiment(lab)

    expt.setup(force_archive=force_archive)


runscript = runcmd
