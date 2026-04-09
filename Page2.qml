import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.15
import QtQuick.Layouts 2.15

Item{
    id: page2root

        ColumnLayout {

            id: infoColumn
            anchors.fill: parent

                Text{
                        id: secondsTextBox
                        Layout.fillWidth: true
                        color: "#800000"
                        text: "Uptime: " + backend.seconds
                        fontSizeMode: Text.Fit
                        font.pixelSize: 1000
                        minimumPixelSize: 10
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
    
                }

                Text{
                        id: rpmTextBox
                        Layout.fillWidth: true
                        color: "#800000"
                        text: "RPM: " + backend.rpm
                        fontSizeMode: Text.Fit
                        font.pixelSize: 1000
                        minimumPixelSize: 10
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
    
                }


        }
}