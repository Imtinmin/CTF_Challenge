<?php $__env->startSection('content'); ?>
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-8">
                <div class="card">
                    <div class="card-header">Dashboard</div>

                    <div class="card-body">
                        <?php if(session('status')): ?>
                            <div class="alert alert-success" role="alert">
                                <?php echo e(session('status')); ?>

                            </div>
                        <?php endif; ?>

                        <form method="POST" action="find">
                            <?php echo csrf_field(); ?>

                            <div class="form-group row">
                                <label for="password"
                                       class="col-md-4 col-form-label text-md-right"><?php echo e(__('Username')); ?></label>

                                <div class="col-md-6">
                                    <input id="username" type="text"
                                           class="form-control<?php echo e($errors->has('password') ? ' is-invalid' : ''); ?>"
                                           name="username" required>
                                </div>
                                <button type="submit" class="btn btn-primary">
                                    <?php echo e(__('Find')); ?>

                                </button>
                            </div>

                        </form>
                        <table class="form-control<?php echo e($errors->has('name') ? ' is-invalid' : ''); ?>" width='100%' border='0' cellspacing='0' cellpadding='0' class='mytable' style='table-layout: fixed'>
                            <tr>
                                <th style="padding-left: 30px;padding-right: 30px" width="%25"><?php echo e(__('Id')); ?></th>
                                <th style="padding-left: 50px;padding-right: 50px"><?php echo e(__('Name')); ?></th>
                                <th style="padding-left: 50px;padding-right: 50px"><?php echo e(__('Laravel_session')); ?></th>
                                <th style="padding-left: 50px;padding-right: 50px"><?php echo e(__('Created_at')); ?></th>
                            </tr>
                            <?php if(!empty($id) and !empty($name) and !empty($laravel_session) and !empty($created_at)): ?>
                                <tr>
                                    <th style="text-align:center;vertical-align:middle"><?php echo e($id); ?></th>
                                    <th style="text-align:center;vertical-align:middle"><?php echo e($name); ?></th>
                                    <th style="word-break:break-all;text-align:center;vertical-align:middle"><?php echo e($laravel_session); ?></th>
                                    <th style="text-align:center;vertical-align:middle"><?php echo e($created_at); ?></th>
                                </tr>
                            <?php endif; ?>
                        </table>

                    </div>
                </div>
            </div>
        </div>
    </div>
<?php $__env->stopSection(); ?>

<?php echo $__env->make('layouts.app', \Illuminate\Support\Arr::except(get_defined_vars(), array('__data', '__path')))->render(); ?>