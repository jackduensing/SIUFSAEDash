import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.15
import QtQuick.Layouts 2.15

Window{

    id: root
    visible: true
    visibility: Window.FullScreen
    title: "infoScreen"

    Item {

        id: rotateItem
        rotation: 90
        width: Screen.height
        height: Screen.width
        anchors.centerIn: parent

        ColumnLayout {

            id: infoColumn
            Layout.fillWidth: true
            Layout.preferredHeight: Screen.width
            Layout.maximumHeight: Screen.width

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

}