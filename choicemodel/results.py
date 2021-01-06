import wx


class Results(wx.Panel):

    def __init__(self, parent=None):
        super(Results, self).__init__(parent=parent)
        self.init_ui()

    def init_ui(self):
        root_sizer = wx.BoxSizer(wx.VERTICAL)

        # Description before calculate buttons
        results_sizer = wx.BoxSizer(wx.HORIZONTAL)
        results_font = wx.Font(wx.FontInfo(12).Bold())
        results_label = wx.StaticText(self, label='Results - Predictions of Potential Market Size')
        results_label.SetFont(results_font)

        results_sizer.Add(results_label, flag=wx.ALL, border=10)

        # calculate service
        calculate_sizer = wx.BoxSizer(wx.HORIZONTAL)
        calculate_service_label = wx.StaticText(self, label='Potential Market Size')

        # service territory
        service_sizer = wx.BoxSizer(wx.VERTICAL)
        service_label = wx.StaticText(self, label='Service Territory')
        service_button = wx.Button(self, label='Calculate')
        service_sizer.Add(service_label)
        service_sizer.Add(service_button, flag=wx.ALL, border=10)

        # zip code
        zip_sizer = wx.BoxSizer(wx.VERTICAL)
        zip_label = wx.StaticText(self, label='By Zip Code')
        zip_button = wx.Button(self, label='Calculate')
        zip_sizer.Add(zip_label)
        zip_sizer.Add(zip_button, flag=wx.ALL, border=10)

        calculate_sizer.Add(calculate_service_label, flag=wx.ALL, border=10)
        calculate_sizer.Add(service_sizer, flag=wx.LEFT, border=20)
        calculate_sizer.Add(zip_sizer, flag=wx.LEFT, border=20)

        root_sizer.Add(results_sizer)
        root_sizer.Add(calculate_sizer)

        self.SetSizer(root_sizer)
