import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.15
import QtQuick.Layouts 2.15

Window{

    id: root
    visible: true
    visibility: Window.FullScreen
    title: "GUI"


    Item {

        id: rotateItem
        rotation: 90
        width: Screen.height
        height: Screen.width
        anchors.centerIn: parent

        SwipeView{

            id: swipeRoot
            anchors.fill: parent
            currentIndex: 0

            Page1 {}
            Page2 {}

        }
    }
}