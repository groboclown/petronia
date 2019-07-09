

class Marshalable(object):
    """
    Implementations must allow for marshalling and unmarshalling
    of the config data.
    """

    def marshal(self):
        """
        The variables "bus" and "id_manager", and the function
        "register" are available to use.

        :return: code to generate the corresponding object.
            Each line of code is an item in a set.
        """
        raise NotImplementedError()
