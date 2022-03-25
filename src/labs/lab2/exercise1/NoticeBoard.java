package labs.lab2.exercise1;

public class NoticeBoard {
    private static NoticeBoard noticeBoard =  null;
    private NoticeBoard(){}
    public static NoticeBoard getNoticeBoard(){
        if (noticeBoard == null) {
            noticeBoard = new NoticeBoard();
        }
        return noticeBoard;
    }
}
