params = {
    'type': 'MBPO',
    'universe': 'gym',
    'domain': 'Humanoid', ## mbpo/env/humanoid.py
    'task': 'v2',

    'kwargs': {
        'epoch_length': 1000,
        'train_every_n_steps': 1,
        'n_train_repeat': 20,
        'eval_render_mode': None,
        'eval_n_episodes': 1,
        'eval_deterministic': True,

        'discount': 0.99,
        'tau': 5e-3,
        'reward_scale': 1.0,
        'model_rollout_freq': 250,
        'model_retain_epochs': 5,
        'rollout_batch_size': 25e3,
        'deterministic': False,
        'num_networks': 7,
        'num_elites': 5,
        'real_ratio': 0.05,
        'target_entropy': -2,
        'max_model_t': None,
        'rollout_schedule': [20, 300, 1, 25],
        'hidden_dim': 400,

        # controller kwargs
        'controller_tau': 500,
        'real_ratio_c': 1.2,
        'model_train_penalty': 0.1,
        'Reward_scale': 300,
        'model_loss_scale': [0, 1],
        'value_loss_scale': [0, 100],
        'policy_error_scale': [0, 10],
        'performance_scale': [0, 3000],
    }
}
