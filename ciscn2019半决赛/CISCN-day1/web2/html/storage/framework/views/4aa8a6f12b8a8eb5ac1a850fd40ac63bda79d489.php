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

                        <?php if(empty($online_upload)): ?>

                            <form method="POST" action="upload" enctype="multipart/form-data">
                                <?php echo csrf_field(); ?>

                                <div class="form-group row">
                                    <label for="password"
                                           class="col-md-4 col-form-label text-md-right"><?php echo e(__('Upload file')); ?></label>

                                    <div class="col-md-6">
                                        <input id="file" type="file"
                                               class="form-control<?php echo e($errors->has('password') ? ' is-invalid' : ''); ?>"
                                               name="file" required>
                                    </div>
                                    <button type="submit" class="btn btn-primary">
                                        <?php echo e(__('Submit')); ?>

                                    </button>
                                </div>

                            </form>

                            <a href="online_upload" class="col-md-4 col-form-label text-md-right"><?php echo e(__('Upload file online')); ?></a>
                            <br>
                            <?php if(!empty($upload_file) and !empty($hash)): ?>
                                <p align="center"><?php echo e(__('Upload successful, but deleted! Only empty file can be uploaded. File name is /var/www/html/uploads/'.$hash.'/'.$hash.".jpg")); ?><p>
                            <?php endif; ?>
                            <?php if(!empty($error)): ?>
                                <p align="center"><?php echo e($error); ?></p>
                            <?php endif; ?>
                        <?php else: ?>
                            <form method="POST" action="online_upload">
                                <?php echo csrf_field(); ?>

                                <div class="form-group row">
                                    <label for="password"
                                           class="col-md-4 col-form-label text-md-right"><?php echo e(__('Picture url')); ?></label>

                                    <div class="col-md-6">
                                        <input id="url" type="text"
                                               class="form-control<?php echo e($errors->has('password') ? ' is-invalid' : ''); ?>"
                                               name="url" required>
                                    </div>
                                    <button type="submit" class="btn btn-primary">
                                        <?php echo e(__('Submit')); ?>

                                    </button>
                                </div>

                            </form>

                            <a href="index" class="col-md-4 col-form-label text-md-right"><?php echo e(__('Upload file')); ?></a>
                            <br>
                            <?php if(!empty($upload_file)): ?>
                                <p align="center"><?php echo e(__('Upload successful, but deleted! Only empty file can be uploaded. File name is /var/www/html/uploads/'.$hash.'/'.$hash.'.jpg')); ?><p>
                            <?php endif; ?>
                            <?php if(!empty($error)): ?>
                                    <p align="center"><?php echo e($error); ?></p>
                            <?php endif; ?>
                        <?php endif; ?>
                    </div>
                </div>
            </div>
        </div>
    </div>
<?php $__env->stopSection(); ?>

<?php echo $__env->make('layouts.app', \Illuminate\Support\Arr::except(get_defined_vars(), array('__data', '__path')))->render(); ?>