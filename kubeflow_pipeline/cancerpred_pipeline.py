import kfp
from kfp import dsl

def data_processing_op():
    return dsl.ContainerOp(
        name='Data Processing',
        image='davidibrahimg/cancerpred:latest',
        command=['python', 'src/data_processing.py'],  # Full path
        arguments=[
            '--output-dir', '/output'  # Explicit output directory
        ],
        file_outputs={
            'processed_data': '/output/processed_data.csv',
            'scaler': '/output/scaler.pkl'
        }
    ).add_volume_mount(
        dsl.VolumeMount('output-volume', '/output')
    )

def model_training_op():
    return dsl.ContainerOp(
        name='Model Training',
        image='davidibrahimg/cancerpred:latest',
        command=['python', 'src/model_training.py'],
        arguments=[
            '--data-path', '/output/processed_data.csv',
            '--scaler-path', '/output/scaler.pkl'
        ]
    ).add_volume_mount(
        dsl.VolumeMount('output-volume', '/output')
    ).after(data_processing_op())

@dsl.pipeline(
    name='Colorectal Cancer Prediction Pipeline',
    description='A pipeline for processing data and training a model for colorectal cancer prediction.'
)
def cancer_prediction_pipeline():
    # Create a shared volume for artifacts
    shared_volume = dsl.PipelineVolume(name='output-volume')
    
    data_processing = data_processing_op().add_pvolumes({
        '/output': shared_volume
    })
    
    model_training = model_training_op().add_pvolumes({
        '/output': shared_volume
    })