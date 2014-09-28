from UMLComponent import UMLComponent
from SelectedBlock import SelectedBlock


class UserCaseComponent(UMLComponent):
    def __init__(self, width, height):
        super(UserCaseComponent, self).__init__(width, height)

    def setup_selected_blocks(self):
        b_size = self.selected_block_size
        position = [[b_size / 2 + self.width / 2, 0],
                    [b_size + self.width, b_size / 2 + self.height / 2],
                    [b_size / 2 + self.width / 2, b_size + self.height],
                    [0, b_size / 2 + self.height / 2]]
        selected_blocks = []
        for i in range(4):
            block = SelectedBlock()
            block.set_size_request(self.selected_block_size, self.selected_block_size)
            self.layout.put(block, position[i][0], position[i][1])
            block.show()
            selected_blocks.append(block)
        return selected_blocks

    def remove_selected_blocks(self):
        for selected_block in self.selected_blocks:
            self.layout.remove(selected_block)

    def rearrange_widget(self):
        # #############
        #     0      #
        #            #
        #3          1#
        #            #
        #     2      #
        ##############
        allocation = self.get_allocation()
        print(allocation.x, allocation.y, allocation.width, allocation.height)
        b_size = self.selected_block_size

        position = [[b_size / 2 + self.width / 2, 0],
                    [b_size + self.width, b_size / 2 + self.height / 2],
                    [b_size / 2 + self.width / 2, b_size + self.height],
                    [0, b_size / 2 + self.height / 2]]
        for i in range(4):
            self.layout.move(self.selected_blocks[i], position[i][0], position[i][1])

    def draw_selected_line(self, cairo_context):
        cairo_context.rectangle(self.selected_block_size, self.selected_block_size, self.width, self.height)
        cairo_context.set_source_rgb(0.5, 0.1, 0.6)
        cairo_context.set_dash(self.selected_line_dashes, 0)
        cairo_context.set_line_width(self.selected_line_width)
        cairo_context.stroke()