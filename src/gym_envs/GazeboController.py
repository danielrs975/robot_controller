import roslibpy

class GazeboController:
    """This module will contains the connection with
    the gazebo nodes in ROS. It will manage all related
    operation with the environment.
        > Reset simulation
        > Move Models
        > etc....
    """
    PERSON_MODEL = "person_standing" # Name of the model to connect to
     
    def __init__(self, client):
        """Constructor of the class

        Args:
            client (WebSocket): Contains the connection with the ROS server
        """
        self.set_position_service = roslibpy.Service(client, '/gazebo/set_model_state', 'gazebo_msgs/SetModelState')
        self.get_position_service = roslibpy.Service(client, '/gazebo/get_model_state', 'gazebo_msgs/GetModelState')

    def get_position(self):
        """Get the actual position of the model (This case is hard wired to the person).

        Returns:
            [type]: [description]
        """
        body = {
            'model_name': self.PERSON_MODEL
        }
        request = roslibpy.ServiceRequest(body)
        return self.get_position_service.call(request)['pose']

    def set_position(self, y_position):
        """Set the new position for a model in the simulation (This case is hard wired to the person).

        Args:
            y_position (Float): The position in the y_axis to move the model
        
        NOTE: We can expand this to the other axis
        """
        body = {
            'model_state': {
                'model_name': self.PERSON_MODEL
            }
        }
        actual_position = self.get_position()
        actual_position['position']['y'] = y_position
        body['model_state']['pose'] = {
            'position': actual_position['position'],
            'orientation': actual_position['orientation']
        }
        request = roslibpy.ServiceRequest(body)
        self.set_position_service.call(request)


# if __name__ == "__main__":
#     HOST = 'localhost'    
#     PORT = 9090
#     client = roslibpy.Ros(host=HOST, port=PORT)
#     cntrl = GazeboController(client)
#     client.run()
#     cntrl.get_position()
#     cntrl.set_position(29.2)