# EVALUATOR - PROGRESS MANAGER
START_CONFIG = 'START_CONFIG'
END_CONFIG = 'END_CONFIG'
END_FINAL_RUN = 'END_FINAL_RUN'
OUTER_FOLD = 'outer_fold'
INNER_FOLD = 'inner_fold'
CONFIG_ID = 'config_id'
RUN_ID = 'run_id'
ELAPSED = 'elapsed'
SEED = 'seed'
GRID_SEARCH = 'grid'
RANDOM_SEARCH = 'random'
NUM_SAMPLES = 'num_samples'
NUM_TASKS = 'n_tasks'
NUM_REHEARSAL_PATTERNS_PER_TASK = 'n_rehearsal_patterns_per_task'
SAMPLE_METHOD = 'sample_method'
DATASET = 'dataset'  # todo remove this from grid and random searches.
CONFIG = 'config'
MODEL_ASSESSMENT = 'MODEL_ASSESSMENT'
FOLDS = 'folds'
AVG_TR_SCORE = 'avg_training_score'
STD_TR_SCORE = 'std_training_score'
AVG_VL_SCORE = 'avg_validation_score'
STD_VL_SCORE = 'std_validation_score'
TR_SCORE = 'training_score'
VL_SCORE = 'validation_score'
BEST_CONFIG = 'best_config'
OUTER_TRAIN = 'outer_train'
OUTER_TEST = 'outer_test'

# STATE
TRAINING = 'training'
EVALUATION = 'evaluation'
VALIDATION = 'validation'
TEST = 'test'
MAIN_LOSS = 'main_loss'
MAIN_SCORE = 'main_score'
LOSSES = 'losses'
SCORES = 'scores'
SCORE = 'score'
MODEL_STATE = 'model_state'
OPTIMIZER_STATE = 'optimizer_state'
SCHEDULER_STATE = 'scheduler_state'
BEST_EPOCH = 'best_epoch'
BEST_EPOCH_RESULTS = 'best_epoch_results'
EPOCH = 'epoch'
STOP_TRAINING = 'stop_training'
LAST_CHECKPOINT_FILENAME = 'last_checkpoint.pth'
BEST_CHECKPOINT_FILENAME = 'best_checkpoint.pth'
BATCH_LOSS_EXTRA = 'batch_loss_extra'

# STRING FORMATTING
TENSORBOARD = 'tensorboard'
EMB_TUPLE_SUBSTR = '_embeddings_tuple'
ATOMIC_SAVE_EXTENSION = '.part'
CLASS_NAME = 'class_name'
ARGS = 'args'
MODEL_STATE_DICT = 'model_state_dict'
OPTIMIZER_STATE_DICT = 'optimizer_state_dict'
AVG = 'avg'
STD = 'std'

# SET UP
CUDA = 'cuda'
PYDGN_RAY_NUM_GPUS_PER_TASK = 'PYDGN_RAY_NUM_GPUS_PER_TASK'
OMP_NUM_THREADS = 'OMP_NUM_THREADS'
MIN = 'min'
MAX = 'max'

# CLI
CONFIG_FILE_CLI_ARGUMENT = '--config-file'
CONFIG_FILE = 'config_file'
DATA_ROOT_CLI_ARGUMENT = '--data-root'
DATA_ROOT = 'data_root'
DATA_SPLITS_FILE_CLI_ARGUMENT = '--data-splits'
DATA_SPLITS_FILE = 'data_splits_file'
DATASET_CLASS_CLI_ARGUMENT = '--dataset-class'
DATASET_CLASS = 'dataset_class'
DATASET_GETTER_CLI_ARGUMENT = '--dataset-getter'
DATASET_GETTER = 'dataset_getter'
DATASET_NAME_CLI_ARGUMENT = '--dataset-name'
DATASET_NAME = 'dataset_name'
DEBUG_CLI_ARGUMENT = '--debug'
DEBUG = 'debug'
DEVICE_CLI_ARGUMENT = '--device'
DEVICE = 'device'
EXPERIMENT_CLI_ARGUMENT = '--experiment'
EXPERIMENT = 'experiment'
FINAL_TRAINING_RUNS_CLI_ARGUMENT = '--final-training-runs'
FINAL_TRAINING_RUNS = 'final_training_runs'
GPUS_PER_TASK_CLI_ARGUMENT = '--gpus-per-task'
GPUS_PER_TASK = 'gpus_per_task'
HIGHER_RESULTS_ARE_BETTER_CLI_ARGUMENT = '--higher-results-are-better'
HIGHER_RESULTS_ARE_BETTER = 'higher_results_are_better'
LOG_EVERY_CLI_ARGUMENT = '--log-every'
LOG_EVERY = 'log_every'
MAX_CPUS_CLI_ARGUMENT = '--max-cpus'
MAX_CPUS = 'max_cpus'
MAX_GPUS_CLI_ARGUMENT = '--max-gpus'
MAX_GPUS = 'max_gpus'
MODEL_CLI_ARGUMENT = '--model'
MODEL = 'model'
NUM_DATALOADER_WORKERS_CLI_ARGUMENT = '--num-dataloader-workers'
NUM_DATALOADER_WORKERS = 'num_dataloader_workers'
PIN_MEMORY_CLI_ARGUMENT = '--pin-memory'
PIN_MEMORY = 'pin_memory'
RESULT_FOLDER_CLI_ARGUMENT = '--result-folder'
RESULT_FOLDER = 'result_folder'
SPLITS_FOLDER_CLI_ARGUMENT = '--splits-folder'
SPLITS_FOLDER = 'splits_folder'
